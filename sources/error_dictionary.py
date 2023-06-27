# ------------------
# | Auto - Project |
# ------------------
# error_dictionary :
# The purpose of the array below is to store all the errors
# that can be encountered during the execution of the program

error_dictionary = {
    "json_management" : {
        "A001" : "Could not open configuration file",
        "A002" : "Could not load configuration data",
        "A003" : "Could not close configuration file",
    },
    "file_creation" : {
        "B001" : "Could not create file",
        "B002" : "Could not create folder",
        "B003" : "Project already exists",
        "B004" : "Could close file",
    },
}

def print_error(type, error_code):
    print(error_dictionary[type][error_code])
    return None
