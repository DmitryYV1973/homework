import os
from typing import Union
from PIL import Image
from pillow_heif import register_heif_opener

class ImageCompressor:
    """
    Класс для сжатия изображений и обработки директорий.
    """

    supported_formats = ('.jpg', '.jpeg', '.png')  # Поддерживаемые форматы файлов

    def __init__(self, quality: int) -> None:
        """
        Конструктор класса для инициализации качества сжатия.

        Args:
            quality (int): Значение качества сжатия (от 1 до 100).
        """
        self.__quality = quality

    @property
    def quality(self) -> int:
        """Геттер для получения значения качества сжатия."""
        return self.__quality

    @quality.setter
    def quality(self, quality: int) -> None:
        """Сеттер для установки значения качества сжатия."""
        if 1 <= quality <= 100:
            self.__quality = quality
        else:
            raise ValueError("Качество должно быть в диапазоне от 1 до 100.")

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.

        Args:
            input_path (str): Путь к исходному изображению.
            output_path (str): Путь для сохранения сжатого изображения.

        Returns:
            None
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.quality)
        print(f"Сжато: {input_path} -> {output_path}")

    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.

        Args:
            directory (str): Путь к директории для обработки.

        Returns:
            None
        """
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + '.heic'
                    self.compress_image(input_path, output_path)

def main(input_path: str) -> None:
    """
    Основная функция программы. Обрабатывает входной путь и запускает сжатие изображений.

    Args:
        input_path (str): Путь к файлу или директории для обработки.

    Returns:
        None
    """
    register_heif_opener()
    input_path = input_path.strip('"')  # Удаляем кавычки, если они есть

    compressor = ImageCompressor(quality=50)  # Создаем экземпляр класса с качеством 50

    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + '.heic'
            compressor.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            print(f"Обрабатываем директорию: {input_path}")
            compressor.process_directory(input_path)
    else:
        print("Указанный путь не существует")

if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    main(user_input)