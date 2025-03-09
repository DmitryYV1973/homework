import abc
import json

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
            with open(self.file_path, r) as file:
                return json.load(file)
            
        def write(self, data) -> None:
            with open(self.file_path, w) as file:
                json.dump(data, file)

        def append(self, data) -> None:
            current_data = self.read()
            current_data.append(data)
            self.write(current_data)

