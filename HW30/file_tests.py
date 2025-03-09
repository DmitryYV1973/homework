import os
import json
import csv

# Импортируем классы из модуля file_classes
from file_classes import JSONFile, TextFile, CSVFile

# Функция для создания тестового файла JSON
def test_json_file():
    json_file = JSONFile('test.json')

    # Записываем начальные данные
    json_file.write([{'name': 'Андрей', 'age': 25}])

    # Добавляем новую запись
    json_file.append({'name': 'Мария', 'age': 30})

    # Читаем данные
    print(json_file.read())


# Функция для создания тестового файла TXT
def test_text_file():
    txt_file = TextFile('test.txt')

    # Тестируем записи
    txt_file.write('Hello, world!')
    print('TXT запись:', txt_file.read())

    # Тестируем добавление
    txt_file.append('\nHello, Python!')
    print('TXT после добавленеия:', txt_file.read())


# Функция для создания тестового файла CSV
def test_csv_file():
    csv_file = CSVFile('test.csv')

    # Тестируем записи
    csv_file.write([['name', 'age'], ['Андрей', '25'], ['Мария', '30']])
    print('CSV запись:', csv_file.read())

    # Тестируем добавление
    csv_file.append(['Иван', '20'])
    print('CSV после добавления:', csv_file.read())

if __name__ == '__main__':
    # Удаляем тестовые файлы, если они уже существуют
    for file in ['test.json', 'test.txt', 'test.csv']:
        if os.path.exists(file):
            os.remove(file)
    # Вызываем тестовые функции
    print('Тестирование JSON файла:')
    test_json_file()
    print('\nТестирование TXT файла:')
    test_text_file()
    print('\nТестирование CSV файла:')
    test_csv_file()