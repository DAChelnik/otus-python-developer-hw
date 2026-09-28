"""Телефонный справочник.

Приложение для управления контактами.
Контакты сохраняются в файле формата JSON.
Каждый контакт содержит имя, телефон, адрес (с детализацией) и комментарий.
Поддерживается поиск по отдельным полям и по всем полям сразу.
"""

# TODO: сделать детализацию адреса, возможно пригодится на выпускное приложение
# TODO: пара имя и телефон должна быть уникальна, необходимо исключить дублирование контактов
# TODO: перед выходом предложить сохранение всех внесённых изменений

import json
from os import path
from typing import Any


def get_next_id(contacts: list[dict[str, Any]]) -> int:
    """Генерирует уникальный ID для нового контакта."""
    if not contacts:
        return 1
    return max(c["id"] for c in contacts) + 1


def open_file(filepath: str) -> list[dict[str, Any]]:
    """Загружает контакты из JSON-файла."""
    if not path.exists(filepath):
        print(f"Файл '{filepath}' не найден. " f"Создан пустой справочник.")
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Ошибка чтения: {exc}")
        return []


def save_to_file(contacts: list[dict[str, Any]], filepath: str) -> None:
    """Сохраняет контакты в JSON-файл."""
    try:
        with open(filepath, "w", encoding="utf-8") as fh:
            json.dump(
                contacts,
                fh,
                ensure_ascii=False,
                indent=4,
            )
    except OSError as exc:
        print(f"Ошибка сохранения: {exc}")
        return
    print(f"Справочник сохранён в '{filepath}'.")


def show_all(contacts: list[dict[str, Any]]) -> None:
    """Выводит все контакты в консоль."""
    if not contacts:
        print("Справочник пуст.")
        return

    for contact in contacts:
        print_one(contact)


def print_one(contact: dict[str, Any]) -> None:
    """Выводит один контакт в читаемом виде."""
    print(
        f"  Имя: {contact.get('name', '')}\n"
        f"  Телефон: {contact.get('phone', '')}\n"
        f"  Адрес: {contact.get('address', '')}\n"
        f"  Комментарий: {contact.get('comment', '')}"
    )
    print("-" * 40)


def add_contact(contacts: list[dict[str, Any]]) -> None:
    """Создаёт новый контакт и добавляет его в список."""
    try:
        print("--- Контактная информация ---")
        name = input("Имя: ")
        phone = input("Телефон: ")
        print("--- Адрес ---")
        address = input()
        print("--- Комментарий ---")
        comment = input("Комментарий: ")
    except ValueError as exc:
        print(f"Ошибка: {exc}")
        return

    contact = {
        "id": get_next_id(contacts),
        "name": name,
        "phone": phone,
        "address": address,
        "comment": comment,
    }
    contacts.append(contact)
    print(f"Контакт добавлен")


def search_contacts(contacts: list[dict[str, Any]]) -> None:
    """Ищет контакты по полям или по всем полям сразу."""
    if not contacts:
        print("Справочник пуст.")
        return
    print(
        "Поиск по:\n"
        "  0 — по всем полям\n"
        "  1 — по имени\n"
        "  2 — по телефону\n"
        "  3 — по комментарию"
    )
    try:
        choice = input("Выберите режим: ")
        mode = int(choice)
    except (ValueError, TypeError):
        print("Ошибка: нужно ввести число.")
        return

    field_map = {
        0: None,
        1: ["name"],
        2: ["phone"],
        3: ["comment"],
    }
    if mode not in field_map:
        print("Ошибка: неизвестный режим поиска.")
        return

    search_text = input("Введите поисковый запрос: ").strip()  # <-- добавили
    if not search_text:
        print("Ошибка: пустой запрос.")
        return

    fields = field_map[mode]
    results = [
        c
        for c in contacts
        if matches_query(c, search_text, fields=fields)  # <-- query → search_text
    ]

    if not results:
        print("Ничего не найдено.")
        return

    for contact in results:
        print_one(contact)


def matches_query(
    contact: dict[str, Any], query: str, fields: list[str] | None = None
) -> bool:
    """Проверяет, содержит ли контакт поисковый запрос."""
    query_lower = query.lower()

    if fields is None:
        searchable = [
            str(contact.get("name", "")),
            str(contact.get("phone", "")),
            str(contact.get("comment", "")),
        ]
        addr = contact.get("address", {})
        if isinstance(addr, dict):
            searchable.extend(str(v) for v in addr.values())
        return any(query_lower in s.lower() for s in searchable)

    for field in fields:
        value = contact.get(field, "")
        if isinstance(value, dict):
            for sub_val in value.values():
                if query_lower in str(sub_val).lower():
                    return True
        elif query_lower in str(value).lower():
            return True
    return False


def edit_contact(contacts: list[dict[str, Any]]) -> None:
    """Редактирует существующий контакт."""
    if not contacts:
        print("Справочник пуст.")
        return

    try:
        raw_id = input("ID контакта для изменения: ")
        contact_id = int(raw_id)
    except (ValueError, TypeError):
        print("Ошибка: ID должен быть числом.")
        return

    contact = find_by_id(contacts, contact_id)
    if contact is None:
        print(f"Контакт с ID {contact_id} не найден.")
        return

    print("Оставьте поле пустым, чтобы не менять значение.")

    try:
        new_name = input(f"Имя [{contact['name']}]: ").strip()
        if new_name:
            contact["name"] = new_name

        new_phone = input(f"Телефон [{contact['phone']}]: ").strip()
        if new_phone:
            contact["phone"] = new_phone

        new_address = input(f"Адрес [{contact['address']}]: ").strip()
        if new_address:
            contact["address"] = new_address

        new_comment = input(f"Комментарий [{contact.get('comment', '')}]: ").strip()
        if new_comment:
            contact["comment"] = new_comment
    except ValueError as exc:
        print(f"Ошибка: {exc}")
        return

    print(f"Контакт ID {contact_id} изменён.")


def find_by_id(
    contacts: list[dict[str, Any]], contact_id: int
) -> dict[str, Any] | None:
    """Ищет контакт по ID."""
    for contact in contacts:
        if contact.get("id") == contact_id:
            return contact
    return None


def remove_contact(contacts: list[dict[str, Any]]) -> None:
    """Удаляет контакт по ID с подтверждением."""
    if not contacts:
        print("Справочник пуст.")
        return

    try:
        raw_id = input("ID контакта для удаления: ")
        contact_id = int(raw_id)
    except (ValueError, TypeError):
        print("Ошибка: ID должен быть числом.")
        return

    contact = find_by_id(contacts, contact_id)
    if contact is None:
        print(f"Контакт с ID {contact_id} не найден.")
        return

    print_one(contact)
    confirm = input("Удалить этот контакт? (y/n): ").lower()
    if confirm != "y":
        print("Удаление отменено.")
        return

    contacts.remove(contact)
    print(f"Контакт ID {contact_id} удалён.")


def show_menu() -> None:
    """Выводит главное меню приложения."""
    print(
        "\n=== Телефонный справочник ===\n"
        "1. Открыть файл\n"
        "2. Сохранить файл\n"
        "3. Показать все контакты\n"
        "4. Создать контакт\n"
        "5. Найти контакт\n"
        "6. Изменить контакт\n"
        "7. Удалить контакт\n"
        "0. Выход"
    )


def main() -> None:
    """Главная точка входа в приложение."""
    contacts: list[dict[str, Any]] = []  # инициализируем пустой список контактов
    filepath = "phonebook.json"
    is_open = False  # установим флаг: файл ещё не открыт

    actions: dict[str, dict[str, Any]] = {
        "1": {
            "label": "Открыть файл",
            "needs_open": False,
        },
        "2": {
            "label": "Сохранить файл",
            "needs_open": True,
        },
        "3": {
            "label": "Показать все",
            "needs_open": True,
        },
        "4": {
            "label": "Создать контакт",
            "needs_open": True,
        },
        "5": {
            "label": "Найти контакт",
            "needs_open": True,
        },
        "6": {
            "label": "Изменить контакт",
            "needs_open": True,
        },
        "7": {
            "label": "Удалить контакт",
            "needs_open": True,
        },
        "0": {
            "label": "Выход",
            "needs_open": False,
        },
    }

    while True:
        show_menu()
        choice: str = input("Выберите действие: ")

        if choice not in actions:
            print("Ошибка: неизвестное действие.")
            continue

        if actions[choice]["needs_open"] and not is_open:
            print("\nСначала откройте или создайте файл (пункт 1).")
            continue

        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            path = input(f"Путь к файлу [{filepath}]: ").strip()
            if path:
                filepath = path
            contacts = open_file(filepath)
            is_open = True  # теперь файл "открыт"
        elif choice == "2":
            path = input(f"Путь к файлу [{filepath}]: ").strip()
            if path:
                filepath = path
            save_to_file(contacts, filepath)
        elif choice == "3":
            show_all(contacts)
        elif choice == "4":
            add_contact(contacts)
        elif choice == "5":
            search_contacts(contacts)
        elif choice == "6":
            edit_contact(contacts)
        elif choice == "7":
            remove_contact(contacts)


if __name__ == "__main__":
    main()
