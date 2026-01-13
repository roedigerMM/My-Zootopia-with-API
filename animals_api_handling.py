import requests

API_KEY = "8iLqRdiWU2U52xeUvMDtwElXp5fZw53mQBPWB67V"

def get_animal_data():
    """ Loads animal data from API and returns it as a JSON. """
    url = "https://api.api-ninjas.com/v1/animals"
    params = {
        "name": "Fox",
        "X-Api-Key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data