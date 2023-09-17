import requests
import json

# URL för att hämta listan över tillgängliga artister
base_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

# Hämta och lista tillgängliga artister
response = requests.get(base_url)
if response.status_code == 200:
    artists = json.loads(response.text)
    print("--- ARTIST DB ---")
    for artist in artists:
        print(artist['name'])
    print("-----------------")
else:
    print("Kunde inte hämta artistlistan")

# Låt användaren välja artist
selected_artist = input("Välj artist: ").strip().lower()

# Sök efter artisten i listan och hämta dess identifiering
artist_id = None
for artist in artists:
    if selected_artist == artist['name'].strip().lower():
        artist_id = artist['id']
        break

# Hämta och skriva ut fördjupande information om den valda artisten
if artist_id:
    artist_url = base_url + artist_id
    response = requests.get(artist_url)
    if response.status_code == 200:
        artist_info = json.loads(response.text)
        print("-----------------")
        print(artist_info['name'])
        print("*****************")
        print("Genres:", artist_info['genres'])
        print("Years active:", artist_info['years_active'])
        print("Members:", artist_info['members'])
        print("-----------------")
    else:
        print("Kunde inte hämta information om artisten")
else:
    print("Artisten hittades inte i listan")

