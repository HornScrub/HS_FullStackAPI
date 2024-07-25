from django.shortcuts import render
import requests
from .config import API_KEY

def get_weather(request):
    city = request.GET.get('city', 'London')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
    }
    return render(request, 'weather/weather.html', context)