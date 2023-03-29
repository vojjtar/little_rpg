import json

def check_saved_characters() -> json:
    with open('./data/characters.json', 'r') as f:
        character_data = json.load(f)

    return character_data


def create_character() -> bool:
    pass