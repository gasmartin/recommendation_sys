import json
from pathlib import Path


ROOT_DIR = Path(__file__).parent
GAMES_PATH = ROOT_DIR / 'games.json'
REVIEWS_PATH = ROOT_DIR / 'reviews.json'


def __read_file(path):
    data = {}

    with path.open() as json_file:
        data = json.load(json_file)

    return data


def __write_file(obj):
    with REVIEWS_PATH.open('w') as json_file:
        json.dump(obj, json_file, indent=4)


def get_games():
    return __read_file(GAMES_PATH)


def get_reviews():
    return __read_file(REVIEWS_PATH)


def save_reviews(reviews):
    __write_file(reviews)
