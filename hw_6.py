from marvel import small_dict

user_input = input('Введите название фильма или его часть: ')

result = []
for title in small_dict:
    if user_input.lower() in title.lower():
        result.append(title)

print(result)
print('-' * 40)

new_dict = {small_dict[key]: key for key in small_dict if user_input.lower() in key.lower()}

print(new_dict)
print('-' * 40)

user_input = int(input('Найдите фильмы, которые вышли после 2024 года: '))

while True:
    new_result = []
    if user_input <= 2024:
        user_input = int(input('Введите год с 2025: '))
    else:
        break

for title, year in small_dict.items():
    if year is None:
        continue
    if year == user_input:
        new_result.append({title: year})

print(new_result)
