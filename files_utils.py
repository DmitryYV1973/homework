import yaml

# Функция для чтения файла в формате JSON
def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, "r", encoding=encoding) as f:
        json_content = f.read()
        return json_content
    
# Функция для записи данных в файл в формате JSON
def write_json(data, file_path: str, encoding: str = "utf-8"):
    with open(file_path, "w", encoding=encoding) as f:
        f.write(data)

# Функция добавления данных в файл в формате JSON
def append_json(data: list[dict], file_path: str, encoding: str = "utf-8"):
    with open(file_path, "a", encoding=encoding) as f:
        f.write(data)

# Функции для работы с CSV
def write_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    with open(file_path, 'w', encoding=encoding) as f:
        writer = f.writer(f, delimiter=delimiter)
        writer.writerows(data)


def append_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    with open(file_path, 'a', encoding=encoding) as f:
        writer = f.writer(f, delimiter=delimiter)
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
def read_yaml(file_path):
    with open(file_path, 'r') as f:
        content = yaml.safe_load(f)
        return content