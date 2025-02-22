class TxtFileHandler:
    """
    Класс для работы с текстовыми файлами (TXT).
    Предоставляет методы для чтения, записи и добавления данных в файлы.
    """

    def read_file(self, filepath: str) -> str:
        """
        Читает содержимое файла и возвращает его в виде строки.
        Возвращает пустую строку, если файл не найден.

        Args:
            filepath (str): Путь к файлу для чтения.

        Returns:
            str: Содержимое файла или пустая строка, если файл не найден.
        """
        try:
            with open(filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Файл '{filepath}' не найден.")
            return ""
        except PermissionError:
            print(f"Нет доступа к файлу '{filepath}'.")
            return ""
        except Exception as e:
            print(f"Произошла ошибка при чтении файла '{filepath}': {e}")
            return ""
        

    def write_file(self, filepath: str, *data: str) -> None:
        """
        Записывает переданные строки в файл.
        Если файл существует, он перезаписывается.

        Args:
            filepath (str): Путь к файлу для записи.
            *data (str): Строки для записи в файл.

        Returns:
            None
        """
        try:
            with open(filepath, 'w') as file:
                for line in data:
                    file.write(line)
        except PermissionError:
            print(f"Нет доступа к файлу '{filepath}'.")
        except Exception as e:
            print(f"Произошла ошибка при записи в файл '{filepath}': {e}")