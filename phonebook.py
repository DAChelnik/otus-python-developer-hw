def load_file() -> None:
    print("загружаем контакты из JSON-файла")
    pass  # Позже здесь будет реализация

def save_to_file() -> None:
    print("сохраняем контакты в JSON-файл")
    pass  # Позже здесь будет реализация

def show_all() -> None:
    print("выводим все контакты в консоль")
    pass  # Позже здесь будет реализация

def add_contact() -> None:
    print("создаём новый контакт и добавляет его в список")
    pass  # Позже здесь будет реализация

def search_contacts() -> None:
    print("Ищет контакты по полям или по всем полям сразу")
    pass  # Позже здесь будет реализация

def edit_contact() -> None:
    print("редактируем существующий контакт")
    pass  # Позже здесь будет реализация

def remove_contact() -> None:
    print("удаляем контакт по ID с подтверждением")
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
    show_menu()


if __name__ == "__main__":
    while True:
        main()
        choice: str = input("Выберите действие: ")
        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            load_file()
        elif choice == "2":
            save_to_file()
        elif choice == "3":
            show_all()
        elif choice == "4":
            add_contact()
        elif choice == "5":
            search_contacts()
        elif choice == "6":
            edit_contact()
        elif choice == "7":
            remove_contact()
