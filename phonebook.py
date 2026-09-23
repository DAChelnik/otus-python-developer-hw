def load_file() -> None:
    """Загружает контакты из JSON-файла."""
    print("\nзагружаем контакты из JSON-файла\n")
    pass  # Позже здесь будет реализация

def save_to_file() -> None:
    """Сохраняет контакты в JSON-файл."""
    print("\nсохраняем контакты в JSON-файл\n")
    pass  # Позже здесь будет реализация

def show_all(contacts) -> None:
    """Выводит все контакты в консоль."""
    print("\nвыводим все контакты в консоль\n")
    if not contacts:
        print("Справочник пуст.")
        return
    pass  # Позже здесь будет реализация

def add_contact(contacts) -> None:
    """Создаёт новый контакт и добавляет его в список."""
    print("\nсоздаём новый контакт и добавляет его в список\n")
    pass  # Позже здесь будет реализация

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
    contacts: list[dict[str, Any]] = [] #инициализируем пустой список контактов
    while True:
        show_menu()
        choice: str = input("Выберите действие: ")
        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            load_file()
        elif choice == "2":
            save_to_file()
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
