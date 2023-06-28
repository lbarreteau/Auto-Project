from json_management import open_and_parse_json_config
from file_creation import init_files

def main():
    config = open_and_parse_json_config()
    if config == None:
        return None
    if init_files(config) == None:
        return None
    return True

if __name__ == "__main__":
    main()