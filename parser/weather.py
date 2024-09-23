from random import choice

from bs4 import BeautifulSoup as bs
from requests import get


def hourly_weather_forecast():
    """ Returns the hourly forecast for the given weather station """
    answer = choice(["Доброе утро солнышко!", "Просыпайся моя булочка!", "С добрый утром мой солёненький кренделёчек"])

    url = 'https://pogoda.mail.ru/prognoz/novosibirsk/24hours/'
    html = bs(get(url, timeout=5).content, 'html.parser')
    main = html.find(class_='p-forecast p-forecast_night js-module')

    data = main.find(class_='p-forecast__title').text
    temperature = f"Температура за бортом {main.find(class_='p-forecast__temperature-value').text}, "
    felt_temperature = f"ощущается как {main.find(class_='p-forecast__data').text}."
    description = f"На улице {main.find(class_='p-forecast__description').text}"

    if "облачность" in description or "облачно" in description:
        icon = "⛅️"
    elif "ясно" in description or "солнечно" in description:
        icon = "☀️"
    elif "гроза" in description:
        icon = "⛈"
    else:
        icon = "🌧"

    return data, answer, temperature, felt_temperature, description, icon


hourly_weather_forecast()
