import flet as ft
import requests

# Функция создания окна приложения
def main(page: ft.Page):
    page.title = 'Погода'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите город', width=400)
    weather_data = ft.Text(value='')

    # Функция для получения данных о погоде
    def get_info(e):
        try:
            if len(user_data.value) < 2:
                return
            
            API_KEY = '173f1af852d5b327a5e955f096ae9f90'
            URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API_KEY}&units=metric'
            res = requests.get(URL).json()
            temp = res['main']['temp']
            feels_like = res['main']['feels_like']
            humidity = res['main']['humidity']
            wind = res['wind']['speed']
            weather_data.value = f'Температура: {str(temp)}°C\nОщущается как: {str(feels_like)}°C\nВлажность: {str(humidity)}%\nСкорость ветра: {str(wind)} м/с'
        except:
            weather_data.value = "Ошибка получения данных"
        page.update()

    # Функция для смены темы
    def change_theme(e):
        # При нажатии на кнопку "Солнышко" меняется тема на светлую
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

# Создание интерфейса
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Текущая погода'),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton('Получить погоду', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)