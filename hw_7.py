from cities import cities_list as cl
from random import choice

name_city = {city["name"] for city in cl}

print('*' * 59)
print('"Игра в города". Чтобы закончить игру, введите слово "стоп"')
print('*' * 59)
players = ["Компьютер", "Игрок"]
current_player_index = 0
last_city = ""
named_cities = set()  # Создаем множество названных городов
symbols_bad = {"ь", "ъ", "ы", "ц", "й"}
game_over = False

number_players = int(input("Введите количество игроков (1 или 2): "))
while number_players > 2:
    print("Максимальное количество игроков — 2.")
    number_players = int(input("Введите количество игроков (1 или 2): "))

while not game_over:
    current_player = players[current_player_index]
    print()
    print(f"{current_player} ходит.")
    print()

    if current_player == "Игрок":
        user_input = input("Город: ")
        if user_input.lower() == "стоп":
            game_over = True
            break

        # Проверка на уже названные города
        if user_input in named_cities:
            print("Этот город уже назван. Попробуйте снова.")
            continue
        
        # Проверка на допустимость города
        if user_input not in name_city:
            print("Город недоступен или не существует. Попробуйте снова.")
            continue

        # Проверка на соответствие последней букве
        if last_city:
            last_letter = last_city[-1]

            # Проверяем, если последняя буква в плохих символах
            if last_letter in symbols_bad:
                # Если последняя буква "ь" или "ъ", то следующая буква - предыдущая
                if last_letter in {"ь", "ъ"}:
                    previous_letter = last_city[-2]  # Предыдущая буква в слове
                else:
                    # Для "ы", "ц", "й" - просто берем предыдущую букву
                    previous_letter = chr(ord(last_letter) - 1)

                print(f'Следующий город должен начинаться на букву "{previous_letter}".')
            else:
                print(f'Следующий город должен начинаться на букву "{last_letter}".')

        # Названные города вносятся во множество named_cities
        named_cities.add(user_input)
        last_city = user_input

    elif current_player == "Компьютер":
        if last_city:
            last_letter = last_city[-1]

            if last_letter in symbols_bad:
                if last_letter in {"ь", "ъ"}:
                    previous_letter = last_city[-2]
                else:
                    previous_letter = chr(ord(last_letter) - 1)

                print(f'Следующий город должен начинаться на букву "{previous_letter}".')
            else:
                previous_letter = last_letter
                print(f'Следующий город должен начинаться на букву "{last_letter}".')
        else:
            previous_letter = choice(list(name_city))[0][0]  # Случайный город для начала

        new_city = None
        for city in name_city:
            if city[0].lower() == previous_letter.lower() and city not in named_cities:
                new_city = city
                break

        if new_city:
            named_cities.add(new_city)
            last_city = new_city
            print(f"Компьютер выбрал город: {new_city}")
        else:
            print("Компьютер не смог найти подходящий город. Вы проиграли!")
            game_over = True
            break

    # Переход к следующему игроку
    current_player_index = (current_player_index + 1) % number_players

if game_over:
    winner = players[(current_player_index - 1) % number_players]
    print(f"Игра окончена. Победитель: {winner}!")

print("Список всех названных городов:")
for city in named_cities:
    print(city, end=' ')