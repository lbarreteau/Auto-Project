# ------------------
# | Auto - Project |
# ------------------
# file_creation :
# The purpose of the functions below are to allow manipulation
# of the json configuration file

import json

def close_json_config(json_file):
    try:
        json_file.close()
    except Exception as e:
        print("Could not close json file")
        print(e)
        return None
    return True

def load_json_config(json_file):
    try:
        json_data = json.load(json_file)
    except Exception as e:
        print("Could not load json data")
        print(e)
        return None
    return json_data

def open_json_config(file_name):
    try:
        json_file = open("../" + file_name, "r")
    except Exception as e:
        print("Could not open configuration file")
        print(e)
        return None
    return json_file

def open_and_parse_json_config(file_name="project-config.json"):
    json_file = open_json_config(file_name)
    if json_file == None:
        return None
    json_data = load_json_config(json_file)
    if json_data == None:
        return None
    if close_json_config(json_file) == None:
        return None
    return json_data
