# test_checker.py
import os
import json
from models import Client, Service, Staff, Appointment
from storage import CarService  # или как вы назвали основной класс

def run_tests():
    print("🔧 Запуск тестов системы CarFix...\n")

    # Очищаем тестовые данные
    data_dir = "data"
    for file in ["clients.json", "services.json", "staff.json", "appointments.json"]:
        path = os.path.join(data_dir, file)
        if os.path.exists(path):
            os.remove(path)

    # Создаём систему
    cs = CarService()
    cs.load_data()  # загружает пустые списки

    print("✅ Тест 1: Добавление клиента")
    client = cs.add_client("Тестовый Клиент", "+70000000000", "Toyota Camry", "Т000ТТ")
    assert client.client_id == 1, "ID клиента должен быть 1"
    assert client.name == "Тестовый Клиент"
    print("   → Клиент добавлен: ID =", client.client_id)

    print("\n✅ Тест 2: Добавление услуги")
    service = cs.add_service("Тестовая мойка", 15, 300.0)
    assert service.service_id == 1
    assert service.name == "Тестовая мойка"
    print("   → Услуга добавлена: ID =", service.service_id)

    print("\n✅ Тест 3: Добавление сотрудника")
    staff = cs.add_staff("Тестовый Мойщик", "Мойщик")
    assert staff.staff_id == 1
    assert staff.position == "Мойщик"
    print("   → Сотрудник добавлен: ID =", staff.staff_id)

    print("\n✅ Тест 4: Создание записи")
    appointment = cs.create_appointment("+70000000000", 1, "2025-06-01 10:00")
    assert appointment is not None, "Запись не создана"
    assert appointment.status == "запланировано"
    assert appointment.staff_id == 1
    print("   → Запись создана: ID =", appointment.appointment_id)

    print("\n✅ Тест 5: Отмена записи")
    success = cs.cancel_appointment(appointment.appointment_id)
    assert success, "Не удалось отменить запись"
    assert cs.get_appointment_by_id(appointment.appointment_id).status == "отменено"
    print("   → Запись отменена")

    print("\n✅ Тест 6: Сохранение и перезагрузка данных")
    cs.save_data()

    # Пересоздаём объект и загружаем
    cs2 = CarService()
    cs2.load_data()

    assert len(cs2.clients) == 1
    assert len(cs2.services) == 1
    assert len(cs2.staff) == 1
    assert len(cs2.appointments) == 1
    assert cs2.appointments[0].status == "отменено"
    print("   → Данные успешно сохранены и загружены")

    print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")

if __name__ == "__main__":
    run_tests()