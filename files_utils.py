import csv
import json
from json import JSONDecodeError
import yaml

def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, "r", encoding=encoding) as f:
        return json.load(f)

def write_json(data, file_path: str, encoding: str = "utf-8"):
    with open(file_path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    try:
        # Сначала читаем существующие данные
        existing_data = []
        try:
            with open(file_path, "r", encoding=encoding) as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            pass
        
        # Если существующие данные не список, создаем новый список
        if not isinstance(existing_data, list):
            existing_data = []
            
        # Добавляем новые данные
        if isinstance(data, list):
            existing_data.extend(data)
        else:
            existing_data.append(data)
            
        # Записываем обновленные данные
        with open(file_path, "w", encoding=encoding) as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)
            
    except (JSONDecodeError, FileNotFoundError, PermissionError) as e:
        print(f"Ошибка при добавлении данных: {e}")

# Функции для работы с CSV
def write_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    with open(file_path, 'w', encoding=encoding) as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerows(data)


def append_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    with open(file_path, 'a', encoding=encoding) as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerows(data)

# Функции для работы с TXT
def read_txt(file_path, encoding: str = "utf-8"):
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()
        return content


def write_txt(data, file_path, encoding: str = "utf-8"):
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(data)


def append_txt(data, file_path, encoding: str = "utf-8"):
    with open(file_path, 'a', encoding=encoding) as f:
        f.write(data)

# Функция для работы с YAML
def read_yaml(file_path, encoding: str = "utf-8"):
    with open(file_path, 'r', encoding=encoding) as f:
        content = yaml.safe_load(f)
        return content