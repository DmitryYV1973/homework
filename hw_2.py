#Задание №1: Конвертация секунд в часы, минуты, секунды

print()
number_seconds = int(input("Введите количество секунд: "))
hours = number_seconds // 3600
minutes = (number_seconds % 3600) // 60
seconds = number_seconds % 60
print()
print(f"В указанном количестве секунд {number_seconds} \nЧасов: {hours:01} \nМинут: {minutes:01} \nСекунд: {seconds:01}")
print()

#Задание №2: Конвертация температуры в градусы Цельсия, Кельвина, Фаренгейта, Реомюра

temperature_Celsius = float(input("Введите температуру в градусах Цельсия: "))
Kelvin_temperature = temperature_Celsius + 273.15
temperature_Fahrenheit = temperature_Celsius * 9 / 5 + 32
Reomur_temperature = temperature_Celsius * 4 / 5
print()
print(f'Если температура в градусах Цельсия равна {temperature_Celsius}°C, то: \nКельвин: {round(Kelvin_temperature, 2)}°K \nФаренгейт: {round(temperature_Fahrenheit, 2)}°F \nРеомюр: {round(Reomur_temperature, 2)}°R')
print()