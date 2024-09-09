## Начало: Сам соновной код находиться ниже он нужен для всех действий в которые ты можешь увидеть в командной строке.






# Импорт библиотеки для работы с консолью и управления выходом из программы
import sys

# Библиотека ASED, где хранятся все модули (Примерная структура)
ASED_library = {
    1: {"name": "Python Basics", "description": "Основы Python, циклы и паттерны."},
    2: {"name": "JavaScript Expressions", "description": "Выражения и операторы в JavaScript."},
    3: {"name": "HTML Fundamentals", "description": "Основы HTML."},
    # Добавьте другие модули по мере необходимости
}

# Приветственное сообщение для пользователя
def welcome_message():
    print("Привет дорогой пользователь, это библиотека ASED!")
    print("Здесь ты можешь найти информацию по Python, JavaScript и HTML.")
    print("Выберите один из вариантов ниже для получения информации:")
    main_menu()

# Главное меню для выбора языка программирования
def main_menu():
    print("\n1) Хочу получить понятия Python")
    print("2) Хочу получить понятия JavaScript")
    print("3) Хочу получить понятия HTML")
    print("4) Выйти из программы")

    choice = input("\nВыберите опцию (введите номер): ")
    if choice == "1":
        module_search_menu("Python")
    elif choice == "2":
        module_search_menu("JavaScript")
    elif choice == "3":
        module_search_menu("HTML")
    elif choice == "4":
        sys.exit()
    else:
        print("Неправильный ввод, попробуйте снова.")
        main_menu()

# Меню для выбора между поиском по модулю или просмотром всех модулей
def module_search_menu(language):
    print(f"\nВы выбрали {language}.")
    print("1) Ввести модуль вручную")
    print("2) Ознакомиться со списком всех модулей")
    print("3) Вернуться к выбору языка")

    choice = input("\nВыберите опцию (введите номер): ")
    if choice == "1":
        manual_module_search(language)
    elif choice == "2":
        list_all_modules(language)
    elif choice == "3":
        main_menu()
    else:
        print("Неправильный ввод, попробуйте снова.")
        module_search_menu(language)

# Ввод модуля вручную по названию или номеру
def manual_module_search(language):
    print(f"\nВы находитесь в разделе {language}.")
    module_input = input("Введите номер или название модуля (или введите 'назад', чтобы вернуться назад): ")
    
    if module_input.lower() == "назад":
        module_search_menu(language)
        return
    
    if module_input.isdigit():
        module_num = int(module_input)
        display_module_info(module_num)
    else:
        for num, module in ASED_library.items():
            if module_input.lower() == module["name"].lower():
                display_module_info(num)
                return
        print("Модуль не найден, попробуйте снова.")
        manual_module_search(language)

# Вывод всех доступных модулей для выбранного языка
def list_all_modules(language):
    print(f"\nСписок доступных модулей для {language}:")
    for num, module in ASED_library.items():
        print(f"{num}: {module['name']} - {module['description']}")
    
    choice = input("\nВведите 'назад', чтобы вернуться к выбору модуля, или выберите модуль вручную: ")
    
    if choice.lower() == "назад":
        module_search_menu(language)
    else:
        manual_module_search(language)

# Функция для отображения информации о выбранном модуле
def display_module_info(module_num):
    if module_num in ASED_library:
        module = ASED_library[module_num]
        print(f"\nМодуль {module_num}: {module['name']}")
        print("Описание модуля:")
        print(module["description"])
        print("\nПример кода в модуле:")
        # Пример кода для демонстрации (можно расширять)
        example_code = "print('Hello, World!')" if module_num == 1 else "console.log('Hello, JavaScript!')"
        print(f"Пример кода:\n{example_code}")
        post_module_menu(module_num)
    else:
        print("Модуль не найден.")
        manual_module_search("Python")

# Меню после отображения информации о модуле
def post_module_menu(module_num):
    print("\n1) Полностью выйти")
    print("2) Найти другой модуль")
    print("3) Перейти к списку модулей")
    print("4) Посмотреть другие языки")
    print("5) Вернуться к предыдущему меню")

    choice = input("\nВыберите опцию (введите номер): ")
    if choice == "1":
        sys.exit()
    elif choice == "2":
        manual_module_search("Python")
    elif choice == "3":
        list_all_modules("Python")
    elif choice == "4":
        main_menu()
    elif choice == "5":
        display_module_info(module_num)
    else:
        print("Неправильный ввод, попробуйте снова.")
        post_module_menu(module_num)

# Запуск программы
if __name__ == "__main__":
    welcome_message()










# Описание самого кода:















## (1) Приветственное сообщение – функция welcome_message() выводит начальное приветствие.

## (2) Главное меню – функция main_menu() позволяет пользователю выбрать язык.

## (3) Поиск модуля – функция module_search_menu() предоставляет выбор между вводом модуля вручную или просмотром всех модулей.

## (4) Ввод модуля – функция manual_module_search() позволяет пользователю искать модуль по названию или номеру.

## (5) Вывод всех модулей – функция list_all_modules() отображает список всех доступных модулей.

## (6) Отображение информации о модуле – функция display_module_info() выводит информацию и пример кода для выбранного модуля.

## (7) Меню после просмотра модуля – функция post_module_menu() позволяет пользователю выбрать дальнейшие действия (выйти, найти другой модуль, вернуться к списку).

## (8) Ты можешь дополнять библиотеку новыми модулями, добавляя их в ASED_library.s