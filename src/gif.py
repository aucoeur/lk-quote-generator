from dotenv import load_dotenv
import os, requests, json, pprint
from random import randint

load_dotenv()

pp = pprint.PrettyPrinter(indent=1)

GIPHY_KEY = os.getenv("GIPHY_KEY")

def gif_random():
    '''Gets a random LetterKenny gif from GIPHY endpoint https://developers.giphy.com/docs/api/endpoint/#random

    Example: https://api.giphy.com/v1/gifs/random?api_key=[GIPHY_KEY]&tag=rpdr&rating=R '''

    url = "https://api.giphy.com/v1/gifs/random"
    params = {
        'api_key': GIPHY_KEY,
        'tag': "letterkenny",
        'rating': "R"
    }

    response = requests.get(url, params)

    json = response.json()

    gif_link = json['data']['images']['original']['webp']
    # pp.pprint(gif_link)
    return gif_link

def gif_random_by_search():
    '''
    Gets a random Letterkenny gif by using a random number from the GIPHY Search Endpoint
    Example: https://api.giphy.com/v1/gifs/search?api_key=[API_KEY]&q=letterkenny
    '''
    url = "https://api.giphy.com/v1/gifs/search"
    params = {
        'api_key': GIPHY_KEY,
        'q': "letterkenny",
        'limit': 10,
        'offset': randint(0, 200),
    }
    response = requests.get(url, params)
    json = response.json()

    rand_index = randint(0, 9)
    data = json['data']
    gif_link = data[rand_index]['images']['original']['webp']
    pp.pprint(json)
    print(rand_index)
    return gif_link
