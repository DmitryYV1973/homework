from files_utils import *

# Тестовые данные
txt_data = "Первая строка\nВторая строка"
json_data = '{"name": "Test", "value": 123}'
csv_data = [
    ["Имя", "Возраст", "Город"],
    ["Мария", "30", "Санкт-Петербург"],
    ["Алексей", "22", "Новосибирск"],
    ["Анна", "28", "Екатеринбург"],
]

yaml_data = """
weather:
    - city: "Москва"
    - temperature: 15
    - condition: "облачно"
"""

# Тестирование TXT
write_txt(txt_data, "test.txt")
content = read_txt("test.txt")
append_txt("\nТретья строка", "test.txt")

# Тестирование JSON
write_json(json_data, "test.json")
json_content = read_json("test.json")

# Добавляем данные в JSON-файл
new_data = {"name": "New Test", "value": 456}
json_content = read_json("test.json")
if isinstance(json_content, list):
    json_content.append(new_data)
else:
    json_content = [json_content, new_data]
write_json(json_content, "test.json")

# Тестирование CSV
write_csv(csv_data, "test.csv")
append_csv([["Петр", "35", "Москва"]], "test.csv")

# Тестирование YAML
with open("test.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_data)
yaml_content = read_yaml("test.yaml")
