import json
import os

# Get the directory path of script.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Join the directory path with the JSON file name
json_file_path = os.path.join(current_dir, 'changeable_aspects.json')

# Load the JSON file
with open(json_file_path) as f:
    ASPECTS = json.load(f)

def get_aspect(identifier: str) -> list[str]:
    aspect_name = ''

    match identifier:
        case 'n':
            aspect_name = 'naming'
        case 'm':
            aspect_name = 'module'
        case 's':
            aspect_name = 'string'
        case 't':
            aspect_name = 'types'
        case 'fs':
            aspect_name = 'function signature'
        case 'st':
            aspect_name = 'statement'
        case 'cl':
            aspect_name = 'collections'
        case 'exp':
            aspect_name = 'expressions'
        case 'exc':
            aspect_name = 'exceptions'

    return ASPECTS[aspect_name]

def get_aspects(identifiers_list: list[str]) -> str:
    aspects_str = ''

    for identifier in identifiers_list:
        current_aspect_list = get_aspect(identifier)
        current_aspect_str = '\n- '.join(current_aspect_list)

        aspects_str += f'- {current_aspect_str}\n'

    return aspects_str

