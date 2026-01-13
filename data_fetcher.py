import requests

API_KEY = "8iLqRdiWU2U52xeUvMDtwElXp5fZw53mQBPWB67V"


def fetch_data(name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics': {
        ...
        }
    },
    """
    url = "https://api.api-ninjas.com/v1/animals"
    params = {
        "name": name,
        "X-Api-Key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data