import json
from os import path
from typing import Any

def open_file(filepath: str) -> list[dict[str, Any]]:
    """Загружает контакты из JSON-файла."""
    if not path.exists(filepath):
        print(
            f"Файл '{filepath}' не найден. "
            f"Создан пустой справочник."
        )
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Ошибка чтения: {exc}")
        return []

def save_to_file(
    contacts: list[dict[str, Any]],
    filepath: str
) -> None:
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
    """Выводит все контакты в консоль.
    """
    if not contacts:
        print("Справочник пуст.")
        return

    for contact in contacts:
        print_contact(contact)

def print_contact(contact: dict[str, Any]) -> None:
    """Выводит один контакт в читаемом виде.
    """
    print(
        f"  Имя: {contact.get('name', '')}\n"
        f"  Телефон: {contact.get('phone', '')}\n"
        f"  Адрес: {contact.get('address', '')}\n"
        f"  Комментарий: {contact.get('comment', '')}"
    )
    print("-" * 40)

def add_contact(contacts: list[dict[str, Any]]) -> bool:
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
        "name": name,
        "phone": phone,
        "address": address,
        "comment": comment,
    }
    contacts.append(contact)
    print(f"Контакт добавлен")

def search_contacts(contacts) -> None:
    """Ищет контакты по полям или по всем полям сразу."""
    print("\nищем контакты по полям или по всем полям сразу")
    if not contacts:
        print("Справочник пуст.")
        return
    pass  # Позже здесь будет реализация

def edit_contact(contacts) -> None:
    """Редактирует существующий контакт."""
    print("\nредактируем существующий контакт")
    if not contacts:
        print("Справочник пуст.")
        return
    pass  # Позже здесь будет реализация

def remove_contact(contacts) -> None:
    """Удаляет контакт по ID с подтверждением."""
    print("удаляем контакт по ID с подтверждением")
    if not contacts:
        print("Справочник пуст.")
        return
    pass  # Позже здесь будет реализация

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
    contacts: list[dict[str, Any]] = [] # инициализируем пустой список контактов
    filepath = "phonebook.json"
    is_open = False # установим флаг: файл ещё не открыт
    while True:
        show_menu()
        choice: str = input("Выберите действие: ")
        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            path = input(
                f"Путь к файлу [{filepath}]: "
            ).strip()
            if path:
                filepath = path
            contacts = open_file(filepath)
            is_open = True # теперь файл "открыт"
        elif choice == "2":
            path = input(
                f"Путь к файлу [{filepath}]: "
            ).strip()
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
        else:
            print("\nОшибка: неизвестное действие.")
            continue

if __name__ == "__main__":
    main()
