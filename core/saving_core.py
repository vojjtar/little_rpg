import json

def check_saved_characters() -> json:
    with open('./data/characters.json', 'r') as f:
        character_data = json.load(f)

    if character_data['characters']:
        for index, character in enumerate(character_data['characters']):
            print(f"{index}. {character['name']}")
    else:
        create_character()
    #return character_data

    #check_saved_characters()

def create_character() -> None:
    with open('./data/character_template.json') as template_file:
        template = json.load(template_file)

    name = input("What will be your name?: ")
    print(f"Hello {name}, I will give you {template['inventory']['health_potion']} potions as a welcome gift.")

    template['name'] = name

    with open('./data/characters.json', 'r') as f:
        character_data = json.load(f)
        character_data["characters"].append(template)

    with open('./data/characters.json', 'w') as f:
        json.dump(character_data, f, indent = 4)

    return