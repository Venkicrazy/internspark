import requests

API_KEY = "bb65ac92280f4e58d1c5ad80de2f43f8"

print("================================")
print("      WEATHER INFORMATION APP")
print("================================")

while True:

    city = input("\nEnter City Name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:

        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:

            print("\nWeather Details")
            print("----------------------------")

            print("City :", data["name"])
            print("Country :", data["sys"]["country"])
            print("Temperature :", data["main"]["temp"], "°C")
            print("Humidity :", data["main"]["humidity"], "%")
            print("Weather :", data["weather"][0]["description"])
            print("Wind Speed :", data["wind"]["speed"], "m/s")

        else:
            print("City not found!")

    except Exception as e:
        print("Error:", e)

    choice = input("\nSearch another city? (y/n): ")

    if choice.lower() != 'y':
        break

print("\nThank You!")