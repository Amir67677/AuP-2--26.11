# ==============================
# ПРАКТИЧЕСКИЕ ЗАДАНИЯ PYTHON
# ==============================

# Задание 1
def task1():
    name = input("Введите имя: ")

    if name != "":
        print("Здравствуйте,", name)
    else:
        print("Имя не введено")


# Задание 2
def task2():
    number = int(input("Введите число: "))

    if number > 0:
        print("Положительное число")
    elif number < 0:
        print("Отрицательное число")
    else:
        print("Число равно нулю")


# Задание 3
def task3():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ")

        if operation == "+":
            print("Результат:", a + b)
        elif operation == "-":
            print("Результат:", a - b)
        elif operation == "*":
            print("Результат:", a * b)
        elif operation == "/":
            if b != 0:
                print("Результат:", a / b)
            else:
                print("Ошибка: деление на ноль!")
        else:
            print("Неизвестная операция")

    except ValueError:
        print("Ошибка: необходимо вводить числа!")


# Задание 4
def task4():
    a = 10
    b = 20
    c = 30

    average = (a + b + c) / 3

    print("Среднее значение:", average)


# Задание 5
def task5():
    def check_even(number):
        if number % 2 == 0:
            return "Чётное"
        else:
            return "Нечётное"

    numbers = [8, 7, 0, -4, -9]

    for number in numbers:
        print(number, "-", check_even(number))


# Задание 6
def task6():
    numbers = [5, 12, 3, 21, 8]

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print("Список:", numbers)
    print("Максимальное число:", maximum)

    # Проверка отрицательных чисел
    negative_numbers = [-10, -3, -25, -7, -1]

    maximum = negative_numbers[0]

    for number in negative_numbers:
        if number > maximum:
            maximum = number

    print("Отрицательный список:", negative_numbers)
    print("Максимальное число:", maximum)


# Задание 7
def task7():
    login_correct = "admin"
    password_correct = "Python123"

    attempts = 3

    while attempts > 0:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login == login_correct and password == password_correct:
            print("Доступ разрешён")
            break
        else:
            attempts -= 1

            if attempts > 0:
                print("Неверные данные.")
                print("Осталось попыток:", attempts)
            else:
                print("Доступ заблокирован")


# ==============================
# ГЛАВНОЕ МЕНЮ
# ==============================

while True:
    print("\n" + "=" * 40)
    print("ПРАКТИЧЕСКИЕ ЗАДАНИЯ ПО PYTHON")
    print("=" * 40)

    print("1. Исправление синтаксических ошибок")
    print("2. Поиск логической ошибки")
    print("3. Тестирование калькулятора")
    print("4. Проверка среднего значения")
    print("5. Тестирование функции")
    print("6. Проверка списка")
    print("7. Авторизация пользователя")
    print("0. Выход")

    choice = input("\nВыберите задание: ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "4":
        task4()
    elif choice == "5":
        task5()
    elif choice == "6":
        task6()
    elif choice == "7":
        task7()
    elif choice == "0":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор!")

    input("\nНажмите Enter для возврата в меню...")
