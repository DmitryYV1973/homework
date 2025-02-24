from dataclasses import dataclass
from typing import List, Dict, Optional
import json
from cities import cities_list

@dataclass
class City:
    """
    Датакласс для хранения информации о городе.
    
    Attributes:
        name (str): Название города
        population (int): Население города
        subject (str): Субъект РФ
        district (str): Федеральный округ
        coords (dict): Координаты города
        is_used (bool): Флаг использования города в игре
    """
    name: str
    population: int
    subject: str
    district: str
    coords: dict
    is_used: bool = False

class JsonFile:
    """
    Класс для работы с JSON файлом городов.
    
    Attributes:
        filename (str): Путь к JSON файлу
    """
    def __init__(self, filename: str):
        self.filename = filename

    def read_data(self) -> List[Dict]:
        """Чтение данных из импортированного модуля"""
        return cities_list

    def write_data(self, data: List[Dict]) -> None:
        """Запись данных в JSON файл"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)