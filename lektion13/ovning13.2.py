import requests

base_url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"

city = input("Enter the name of the city for which you want forecasts: ")

url = base_url + city.lower()

response = requests.get(url)

# Kontrollera om förfrågan lyckades
if response.status_code == 200:
    # Konvertera API-svaret till JSON-format
    data = response.json()

    # Hämta och presentera väderprognoserna
    forecasts = data['forecasts']

    print("----------------------")
    print("FORECASTS")
    print("**********************")
    for forecast in forecasts:
        print(f"{forecast['date']} {forecast['forecast']}")
    print("----------------------")
else:
    print("An error occurred while fetching data from the API.")