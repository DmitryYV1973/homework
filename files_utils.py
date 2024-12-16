import yaml

# Функция для чтения файла в формате JSON
def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, "r", encoding=encoding) as f:
        json_content = f.read()
        return json_content