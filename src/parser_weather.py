from bs4 import BeautifulSoup as bs
from requests import get


def hourly_weather_forecast():
    url = 'https://pogoda.mail.ru/prognoz/novosibirsk/24hours/'
    html = bs(get(url, timeout=5).content, 'html.parser')
    main = html.find(class_='p-forecast p-forecast_night js-module')

    data = main.find(class_='p-forecast__title').text
    temperature = main.find(class_='p-forecast__temperature-value').text
    description = main.find(class_='p-forecast__description').text
    felt_temperature = main.find(class_='p-forecast__item').text

    return data, temperature, felt_temperature, description
