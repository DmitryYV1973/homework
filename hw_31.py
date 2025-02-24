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

class CitiesSerializer:
    """
    Класс для сериализации данных о городах.
    Преобразует словари с данными городов в объекты класса City.
    
    Attributes:
        cities (List[City]): Список объектов городов
    """
    def __init__(self, city_data: List[Dict]):
        self.cities = [City(**city) for city in city_data]

    def get_all_cities(self) -> List[City]:
        """Возвращает список всех городов"""
        return self.cities

class CityGame:
    """
    Основной класс игровой логики.
    
    Управляет ходом игры, проверяет правильность ходов,
    определяет ответы компьютера.
    
    Attributes:
        cities (List[City]): Список городов для игры
        last_letter (Optional[str]): Последняя буква предыдущего города
        current_city (Optional[City]): Текущий город в игре
    """
    def __init__(self, cities_serializer: CitiesSerializer):
        self.cities = cities_serializer.get_all_cities()
        self.last_letter: Optional[str] = None
        self.current_city: Optional[City] = None

    def start_game(self) -> str:
        self.current_city = self.cities[0]
        self.current_city.is_used = True
        self.last_letter = self.current_city.name[-1].upper()
        return f"Компьютер называет город: {self.current_city.name}"

    def human_turn(self, city_input: str) -> str:
        city_input = city_input.strip().title()
        
        if not city_input.startswith(self.last_letter):
            return f"Город должен начинаться на букву {self.last_letter}"

        city = next((c for c in self.cities if c.name == city_input), None)
        if not city:
            return "Такого города нет в списке"
        
        if city.is_used:
            return "Этот город уже был использован"

        city.is_used = True
        # Если город заканчивается на й, ь или ы, берём предпоследнюю букву
        if city.name[-1].lower() in ['й', 'ь', 'ы']:
            self.last_letter = city.name[-2].upper()
        else:
            self.last_letter = city.name[-1].upper()
    
        self.current_city = city
        return self.computer_turn()

    def computer_turn(self) -> str:
        available_city = next(
            (c for c in self.cities 
        if c.name.startswith(self.last_letter) and not c.is_used),
            None
        )
        
        if not available_city:
            return "Компьютер не может найти подходящий город. Вы победили!"

        available_city.is_used = True
        self.current_city = available_city
        
        # Если город заканчивается на й, ь или ы, берём предпоследнюю букву
        if available_city.name[-1].lower() in ['й', 'ь', 'ы']:
            self.last_letter = available_city.name[-2].upper()
        else:
            self.last_letter = available_city.name[-1].upper()
        
        return f"Компьютер называет город: {available_city.name}"

    def check_game_over(self) -> bool:
        return all(city.is_used for city in self.cities)
    
class GameManager:
    """
    Класс управления игровым процессом.
    
    Организует взаимодействие между компонентами игры,
    обрабатывает пользовательский ввод и управляет игровым циклом.
    
    Attributes:
        json_file (JsonFile): Объект для работы с JSON
        cities_serializer (CitiesSerializer): Сериализатор городов
        city_game (CityGame): Объект игровой логики
    """
    def __init__(self, json_file: JsonFile, cities_serializer: CitiesSerializer, city_game: CityGame):
        self.json_file = json_file
        self.cities_serializer = cities_serializer
        self.city_game = city_game

    def __call__(self):
        self.run_game()

    def run_game(self):
        print("Добро пожаловать в игру 'Города'!")
        print("Введите 'выход', чтобы завершить игру.")
        print()
        print(self.city_game.start_game())

        while not self.city_game.check_game_over():
            city_input = input("\nВведите название города: ")
            if city_input.lower() == 'выход':
                break
                
            result = self.city_game.human_turn(city_input)
            print(result)
            
            if "победили" in result:
                break

        print("\nИгра завершена!")

if __name__ == "__main__":
    json_file = JsonFile("cities.json")
    cities_serializer = CitiesSerializer(json_file.read_data())
    city_game = CityGame(cities_serializer)
    game_manager = GameManager(json_file, cities_serializer, city_game)
    game_manager()