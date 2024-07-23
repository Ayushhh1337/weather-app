import requests;

api_key = '98c3830481cffac0ad46ce6470cdaf26';

user_input = input("enter your city name: ");

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}");
if weather_data.json()['cod'] == '404':
    print("No City Found");
else:
    weather = weather_data.json()['weather'][0]['main'];
    temp = round(weather_data.json()['main']['temp']);

    print(f"The weather in {user_input} is: {weather}");
    print(f"The temperature in {user_input} is: {temp}ºF");