import json
import random

from operator import itemgetter

def get_data():
    try:
        with open("game_data.json", "r") as game_data:
            data = json.loads(game_data.read())
    except FileNotFoundError:
        data = []
    
    item_number = random.randint(0, len(data)-1)
    return data[item_number]

def play_game():
    data = get_data()
    print(f"Game: What is the capital city of {data.get('country')}?")
    user_input = input("User: ")

    if user_input.lower() == data.get("capital").lower():
        print(f"This is correct!")
    else:
        print("This is wrong!")

