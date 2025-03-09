import abc
import json
import csv

class AbstractFile(abc.ABC):
    '''Абстрактный класс для работы с файлами'''
    @abc.abstractmethod
    def read(self):
        '''Читаем данные из файла'''
        pass

    @abc.abstractmethod
    def write(self, data):
        '''Записываем данные в файл'''
        pass

    @abc.abstractmethod
    def append(self, data):
        '''Записываем данные в файл'''
        pass


    class JSONFile(AbstractFile):
        '''Класс для работы с файлами в формате JSON'''
        def __init__(self, file_path) -> None:
            self.file_path = file_path

        def read(self) -> dict:
            with open(self.file_path, 'r') as file:
                return json.load(file)
            
        def write(self, data) -> None:
            with open(self.file_path, 'w') as file:
                json.dump(data, file)

        def append(self, data) -> None:
            current_data = self.read()
            if isinstance(current_data, list):
                current_data.append(data)
            else:
                raise ValueError('Данные в файле должны быть в формате списка')
            self.write(current_data)


class TextFile(AbstractFile):
    '''Класс для работы с файлами в формате TXT'''
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def read(self) -> str:
        with open(self.file_path, 'r') as file:
            return file.read()
        
    def write(self, data) -> None:
        with open(self.file_path, 'w') as file:
            file.write(data)

    def append(self, data) -> None:
        with open(self.file_path, 'a') as file:
            file.write(data)


class CSVFile(AbstractFile):
    '''Класс для работы с файлами в формате CSV'''
    def __init__(self, file_path) -> None:
        self.file_path = file_path

        def read(self) -> list:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                return list(reader)
            
        def write(self, data) -> None:
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)

        def append(self, data) -> None:
            with open(self.file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)