# ------------------
# | Auto - Project |
# ------------------
# file_creation :
# The purpose of the functions below are to allow manipulation
# of the json configuration file

import json

def open_json_config(file_name="project-config.json"):
    try:
        json_file = open("../" + file_name)
    except:
        print("Could not open configuration file")