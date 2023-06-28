# ------------------
# | Auto - Project |
# ------------------
# file_creation :
# The purpose of the functions below are to allow the
# creation of the requested files in order to fill them afterwards

import os

def create_file(file_name, path, header):
    try:
        file = open(path + file_name, "w")
    except Exception as e:
        print("file_creation", "B001")
        print(e)
        return None
    if header != "":
        try:
            file.write(header + "\n")
        except Exception as e:
            print("file_creation", "B005")
            print(e)
            return None
    try:
        file.close()
    except Exception as e:
        print("file_creation", "B004")
        print(e)
        return None
    return file

def create_folder(folder_name, path):
    try:
        os.mkdir(path + "/" + folder_name)
    except Exception as e:
        print("file_creation", "B002")
        print(e)
        return None
    return True

def format_global_variables(name, config):
    if name.find("NAME_OF_THE_PROJECT") != -1:
        name = name.replace("NAME_OF_THE_PROJECT", config["name_of_the_project"])
    if name.find("EXTENSION_SOURCE") != -1:
        name = name.replace("EXTENSION_SOURCE", config["extension_source"])
    if name.find("EXTENSION_HEADER") != -1:
        name = name.replace("EXTENSION_HEADER", config["extension_header"])
    return name

def check_if_project_already_exists(config):
    path = os.path.expanduser(config["global"]["path"])
    name_of_the_project = config["global"]["name_of_the_project"]
    if os.path.exists(path + "/" + name_of_the_project):
        print("file_creation", "B003")
        return None
    return True

def init_files(config):
    path = os.path.expanduser(config["global"]["path"])
    name_of_the_project = config["global"]["name_of_the_project"]
    create_folder(name_of_the_project, path)
    path = path + "/" + name_of_the_project
    for folder in config["files"]:
        if create_folder(folder, path) == None:
            return None
        for file in config["files"][folder]:
            file = format_global_variables(file, config["global"])
            header = ""
            if file.find(config["global"]["extension_source"]) != -1 or
            file.find(config["global"]["extension_header"]) != -1:
                header = config["global"]["header"]
                header = format_global_variables(header, config["global"])
            if create_file(file, path + "/" + folder + "/", header) == None:
                return None
    return True
