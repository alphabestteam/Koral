"""
File Handling: 
1. If we want to get a big chunk of data , it would be more efficient to write it in a file and not in the code, because it can make the code clumsy and uncomfortable to read. For example, if i have a company that contains 100 people, it wouldn't be efficient to save 100 variables for each worker and their data ( age, salary , role..) . 
2. To open a file, we need to use the open() function, which have 2 arguments, "filename" and "mode" with the syntax of: "open(filename, mode)". the "mode" argument has 4 methods: 
    - "r" - read, opens a file for reading and sends an error if the file doesn't exists
    - "a" - append, opens a file for appending and creates the file if it doesn't exists
    - "w" - write, opens a file for writing and creates the file if it doesn't exists
    - "x" - creates a the specified file and sends an error if the file doesn't exists
    - the main difference between "a" and "w" is that "w" method overwrite the data that is current in the file and "a" appends data to the current data in the file
"""

import configparser
import json

def ex3():
    # The function reads information from a file, prints it to the screen, and writes new content into a file

    with open("config.txt", "r") as fd1:
        print(fd1.read())

    with open("config.txt", "a") as fd2:
        fd2.write("my name is...")


def ex4():
    # The function reads the 'data' field, and make it uppercase. also, if silent = True, the function will print the content of 'data' field  and anyway, the function will save the "data" uppercase content to a file

    config = configparser.ConfigParser()
    config.add_section('header')
    config.set('header','data', 'koral is the queen')
    config.set('header', 'silent', 'True')

    with open("textfile.txt", 'w') as config_file: # To create the config file with the header and property's 
        config.write(config_file)

    config.read("textfile.txt")
    data_var = config['header']['data']
    config.set('header', 'data', data_var.upper()) # Updating the config file to change the data fields value to uppercase
    data_var = data_var.upper()

    with open("textfile.txt", "w") as cf1:  
        config.write(cf1) # Writing all the changes to the file 

    if config['header']['silent'] == "True":
        print(data_var)


"""
JSON:
1. JSON is a java script object notation. JSON is a way of storing and transferring data. The JSON syntax is very similar to a dictionary, it contains propertys with {key : value} mapping  
2. To use json in python, we would have to import the "json" module ("import json"). the main function that JSON uses are "loads" and "dumps". loads() parses a JSON string and returns a dictionary ( load() reads a file containing JSON object) and dumps() is the opposite to loads(), it converts a dictionary to a JSON string.
"""

def json_ex():
    # The function writes a JSONfile that contains the name, age and city of a specific person ( or a sponge ). The function reads the file, converts it to a dictionary and prints it. also, the function changes the fields and saves them to another file. 

    person = {
    "name": "Spongebob",
    "age": 12,
      "city": "Bikini Bottom"
    }
    json_person = json.dumps(person, indent=4)

    with open("json_person_file.txt", 'w') as fd: # To create the json file 
        json.dump(person, fd, indent=4)

    with open("json_person_file.txt", 'r') as fd1: # To read the json file 
        json_dict = json.load(fd1)
        print(json_dict)

    json_dict["name"] = "koral"
    json_dict["age"] = 18
    json_dict["city"] = "no where"
    with open("json_person_other.txt", 'w') as fd2: # To create another json file 
        json.dump(json_dict, fd2, indent=4)
        

if __name__ == "__main__":ex4()