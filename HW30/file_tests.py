import os
import json
import csv

# Импортируем классы из модуля file_classes
from file_classes import JSONFile, TextFile, CSVFile

# Функция для создания тестового файла JSON
def test_json_file():
    json_file = JSONFile('test.json')

    # Тестируем записи
    json_file.write({'name': 'Андрей', 'age': 25})
    print('JSON запись:', json_file.read())

    # Тестируем добавление
    json_file.append({'name': 'Мария', 'age': 30})
    print('JSON после добавленеия:', json_file.read())


# Функция для создания тестового файла TXT
def test_text_file():
    txt_file = TextFile('test.txt')

    # Тестируем записи
    txt_file.write('Hello, world!')
    print('TXT запись:', txt_file.read())

    # Тестируем добавление
    txt_file.append('Hello, Python!')
    print('TXT после добавленеия:', txt_file.read())