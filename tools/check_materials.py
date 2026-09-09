"""Статическая проверка комплекта и запуск демонстраций. Без сторонних пакетов."""
import ast
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
SKIP = {'.git', '.venv', '__pycache__', 'student_work', 'submission', 'submissions'}

def files(suffix):
    return [p for p in ROOT.rglob('*' + suffix) if not any(part in SKIP for part in p.relative_to(ROOT).parts)]

def check():
    if sys.version_info < (3, 11):
        errors.append('Нужен Python 3.11+')
    for n in range(1, 8):
        required = [f'lectures/{n:02d}/README.md', f'slides/lecture_{n:02d}.pptx',
                    f'slides/lecture_{n:02d}.html', f'slides/lecture_{n:02d}.md', f'slides/source/lecture_{n:02d}.json']
        for name in required:
            if not (ROOT / name).is_file(): errors.append(f'Отсутствует {name}')
    for n in range(1, 15):
        if not (ROOT / f'practices/{n:02d}/README.md').is_file(): errors.append(f'Нет практики {n}')
        if n <= 12:
            for name in ['starter.py','tests.py','check.py']:
                if not (ROOT / f'practices/{n:02d}' / name).is_file(): errors.append(f'Нет {n}/{name}')
    for p in files('.py'):
        try: ast.parse(p.read_text(encoding='utf-8'), filename=str(p))
        except SyntaxError as error: errors.append(str(error))
    for p in files('.md'):
        content = re.sub(r'```.*?```', '', p.read_text(encoding='utf-8'), flags=re.S)
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if re.match(r'^[a-z]+:', link) or link.startswith('#'): continue
            target = unquote(link.split('#',1)[0].strip('<>'))
            if target and not (p.parent / target).exists(): errors.append(f'Битая ссылка {p.relative_to(ROOT)}: {link}')
    manifest = json.loads((ROOT / 'lectures/examples_manifest.json').read_text(encoding='utf-8'))
    if len(manifest) != 49: errors.append(f'Ожидалось 49 демонстраций, найдено {len(manifest)}')
    for case in manifest:
        try:
            result = subprocess.run([sys.executable, str(ROOT / case['path'])], cwd=ROOT,
                                    text=True, encoding='utf-8', capture_output=True, timeout=10)
            if result.returncode or result.stdout != case['stdout']:
                errors.append(f'Демонстрация {case["path"]}: {result.returncode}, вывод={result.stdout!r}, ожидание={case["stdout"]!r}, stderr={result.stderr}')
        except subprocess.TimeoutExpired: errors.append(f'Тайм-аут: {case["path"]}')
    for n in range(1,8):
        deck = ROOT / f'slides/lecture_{n:02d}.pptx'
        source = ROOT / f'slides/source/lecture_{n:02d}.json'
        if not deck.is_file(): continue
        try:
            slides = json.loads(source.read_text(encoding='utf-8'))
            with zipfile.ZipFile(deck) as z:
                names = [name for name in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)]
                if len(names) != len(slides): errors.append(f'{deck.name}: неверное число слайдов')
                for name in names: ET.fromstring(z.read(name))
                if z.testzip() is not None: errors.append(f'{deck.name}: повреждён ZIP')
            html = (ROOT / f'slides/lecture_{n:02d}.html').read_text(encoding='utf-8')
            if html.count('<section class="slide ') != len(slides): errors.append(f'{deck.name}: HTML не соответствует числу слайдов')
        except (ValueError, zipfile.BadZipFile, ET.ParseError) as error: errors.append(f'{deck.name}: {error}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'OK: 7 лекций, 14 практик, 49 демонстраций, 7 комплектов презентаций; синтаксис и локальные ссылки проверены.')
    print('Заготовки практик и проекта не проверяются как готовые решения. Используйте соответствующие check.py и semester/run_tests.py.')
    return 0

if __name__ == '__main__':
    raise SystemExit(check())
