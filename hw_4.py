import os

os.system('cls')

user_text = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))

# Алфавит русского языка с учетом регистра
alphabet_ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_ru_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Начало и конец диапазонов для английского алфавита
upper_start = ord('A')
upper_end = ord('Z')
lower_start = ord('a')
lower_end = ord('z')

# Длина алфавита английского языка
alphabet_length_en = 26

result = ""

for char in user_text:
    index = (alphabet_ru_upper.index(char) if char in alphabet_ru_upper else alphabet_ru_lower.index(char)
            if char in alphabet_ru_lower else None)

    if index is not None:  # Если символ является буквой
        new_index = (index + shift) % (len(alphabet_ru_upper) if char in alphabet_ru_upper else len(alphabet_ru_lower))
        result += (alphabet_ru_upper[new_index] if char in alphabet_ru_upper else alphabet_ru_lower[new_index])
    elif 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            # Обработка английского алфавита функциями ord(), chr()
        start = upper_start if char.isupper() else lower_start
        offset = (ord(char) - start + shift) % alphabet_length_en
        new_char = chr(start + offset)
        result += new_char
    else:
        result += char  # Добавляем символ, если он не является буквой

print(result)
