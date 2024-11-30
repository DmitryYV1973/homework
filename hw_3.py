print()
print("Добро пожаловать в программу определения уровня знаний!")
print("=" * 55)
name = input("Введите ваше имя: ")
grade_input = input("Введите вашу оценку: ")
print()
if grade_input.isdigit():
    grade = int(grade_input)
    if grade >= 1 and grade <= 3:
        print(f"{name}, ваш уровень Начальный.")
        print()
    elif grade >= 4 and grade <= 6:
        print(f"{name}, ваш уровень Средний.")
        print()
    elif grade >= 7 and grade <= 9:
        print(f"{name}, ваш уровень Достаточный.")
        print()
    elif grade >= 10 and grade <= 12:
        print(f"{name}, ваш уровень Высокий.")
        print()
    else:
        print("Оценка не корректна.")
        print()