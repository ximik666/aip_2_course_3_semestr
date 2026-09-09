"""Сборка автономных HTML-презентаций из slides/source/*.json. Только stdlib."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
CSS = """
:root { color-scheme: light; font-family: Arial, sans-serif; }
* { box-sizing: border-box; }
body { margin: 0; background: #e8edf0; color: #122d3f; }
main { min-height: 100vh; display: grid; place-items: center; padding: 24px 24px 72px; }
.slide { display: none; width: min(1180px, 100%); aspect-ratio: 16 / 9; padding: 5% 6%; background: #fafbfc; overflow: auto; }
.slide.active { display: flex; flex-direction: column; }
.slide.cover { background: #122d3f; color: #fff; justify-content: center; }
h1 { font-size: clamp(26px, 3.4vw, 48px); line-height: 1.16; margin: 0 0 34px; }
.cover h1 { font-size: clamp(30px, 4.4vw, 62px); }
p { font-size: clamp(20px, 2.4vw, 34px); line-height: 1.4; margin: 0 0 22px; }
pre { margin: 0; white-space: pre-wrap; overflow-wrap: anywhere; font: clamp(15px, 1.8vw, 27px)/1.38 'Courier New', monospace; color: #174b5b; }
.count { margin-top: auto; padding-top: 20px; font-size: 16px; color: #657e8c; }
.cover .count { color: #a9cad6; }
nav { position: fixed; bottom: 0; left: 0; width: 100%; display: flex; justify-content: center; flex-wrap: wrap; gap: 10px; padding: 10px; background: #fff; border-top: 1px solid #c9d5dc; }
button { font: inherit; color: #122d3f; border: 1px solid #8ca7b5; padding: 8px 15px; background: white; cursor: pointer; }
button:focus-visible { outline: 3px solid #008f80; }
button:disabled { opacity: .45; cursor: default; }
aside { position: fixed; inset: 8% 8% 90px; background: #fff; padding: 30px; overflow: auto; box-shadow: 0 0 0 100vmax #0008; z-index: 2; }
aside[hidden] { display: none; }
aside h2 { margin-top: 0; }
aside pre { font: 18px/1.6 Arial, sans-serif; color: #122d3f; }
@media print {
 @page { size: landscape; margin: 0; }
 body, main { background: white; padding: 0; display: block; }
 .slide, .slide.active { display: flex; width: 100vw; height: 100vh; aspect-ratio: auto; break-after: page; padding: 40px 60px; overflow: visible; }
 nav, aside { display: none !important; }
 h1 { font-size: 32pt; } p { font-size: 22pt; } pre { font-size: 16pt; }
}
"""
SCRIPT = """
const slides = [...document.querySelectorAll('.slide')];
let index = Math.max(0, Math.min(slides.length-1, (parseInt(location.hash.slice(1),10)||1)-1));
const notes = document.querySelector('aside');
function show() {
 slides.forEach((s,i)=>{s.classList.toggle('active',i===index); s.setAttribute('aria-hidden', i===index?'false':'true');});
 document.querySelector('#status').textContent = `${index+1} / ${slides.length}`;
 document.querySelector('#prev').disabled=index===0;
 document.querySelector('#next').disabled=index===slides.length-1;
 document.querySelector('#note-text').textContent=slides[index].querySelector('template').content.textContent;
 history.replaceState(null,'',`#${index+1}`);
}
function move(delta){index=Math.max(0,Math.min(slides.length-1,index+delta));show();}
function toggleNotes(){notes.hidden=!notes.hidden;document.querySelector('#notes').setAttribute('aria-expanded',String(!notes.hidden));}
function fullscreen(){if(!document.fullscreenElement) document.documentElement.requestFullscreen?.().catch(()=>{});else document.exitFullscreen?.();}
document.querySelector('#prev').onclick=()=>move(-1);
document.querySelector('#next').onclick=()=>move(1);
document.querySelector('#notes').onclick=toggleNotes;
document.querySelector('#close').onclick=toggleNotes;
document.querySelector('#full').onclick=fullscreen;
document.addEventListener('keydown',e=>{
 if(e.key==='Escape'&&!notes.hidden){toggleNotes();return;}
 if(e.key==='ArrowRight'||e.key==='PageDown'){e.preventDefault();move(1);}
 if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();move(-1);}
 if(e.key.toLowerCase()==='n')toggleNotes();
 if(e.key.toLowerCase()==='f')fullscreen();
});
show();
"""

def build():
    for source in sorted((ROOT / 'slides' / 'source').glob('lecture_*.json')):
        slides = json.loads(source.read_text(encoding='utf-8'))
        sections = []
        for index, slide in enumerate(slides, 1):
            title = html.escape(slide['title'])
            if slide['kind'] == 'code':
                body = '<pre><code>' + html.escape(slide['body']) + '</code></pre>'
            else:
                body = ''.join('<p>' + html.escape(p).replace('\n', '<br>') + '</p>' for p in slide['body'].split('\n\n'))
            notes = html.escape(slide['notes'])
            sections.append(f'<section class="slide {slide["kind"]}" aria-label="Слайд {index}"><h1>{title}</h1>{body}<div class="count">{index} / {len(slides)}</div><template>{notes}</template></section>')
        page = '<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(slides[0]['title']) + '</title><style>' + CSS + '</style></head><body><main>' + ''.join(sections) + '</main><nav aria-label="Управление презентацией"><button id="prev" aria-label="Предыдущий слайд">← Назад</button><span id="status" aria-live="polite"></span><button id="next" aria-label="Следующий слайд">Далее →</button><button id="notes" aria-expanded="false">Заметки (N)</button><button id="full">Полный экран (F)</button></nav><aside hidden aria-label="Заметки преподавателя"><button id="close">Закрыть</button><h2>Заметки преподавателя</h2><pre id="note-text"></pre></aside><script>' + SCRIPT + '</script></body></html>'
        target = source.parent.parent / (source.stem + '.html')
        target.write_text(page, encoding='utf-8')
        print(target.name)

if __name__ == '__main__':
    build()
