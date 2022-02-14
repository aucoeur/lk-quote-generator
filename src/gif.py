from dotenv import load_dotenv
import os, requests, json, pprint

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
    pp.pprint(gif_link)
    return gif_link
