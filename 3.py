# 51 The code produces an error. Please understand the error and try to fix it

# print(type("Hey".replace("ey","i")[-1])     # SyntaxError: unexpected EOF while parsing
print(type("Hey".replace("ey","i")[-1]))



# 52 The code is supposed to ask the user to enter their name and surname and then it prints out those user submitted values. Instead, the code throws a TypeError. Please fix it so that the expected output is printed out.

firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
# print("Your first name is %s and your second name is %s" % firstname, secondname) # TypeError: not enough arguments for format string
# Expected output: 
# Your first name is John and your second name is Smith 
print("Your first name is %s and your second name is %s" % (firstname, secondname)) # tuple expected after %


# 53 Print out the last name of the second employee.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output: 
# Smith 

print(d["employees"][1]["lastName"])


# 54 Please update the dictionary by changing the last name of the second employee from Smith to Smooth or to whatever takes your fancy.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
# Expected output: 

# d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                 {"firstName": "Anna", "lastName": "Smooth"},
#                 {"firstName": "Peter", "lastName": "Jones"}],
# "owners":[{"firstName": "Jack", "lastName": "Petter"},
#           {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"][1]["lastName"] = "Smooth"
print(d)


# 55 Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# Expected output: 
# {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#                {'firstName': 'Anna', 'lastName': 'Smith'},
#                {'firstName': 'Peter', 'lastName': 'Jones'},
#                {'firstName': 'Albert', 'lastName': 'Bert'}],
#  'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#             {'firstName': 'Jessy', 'lastName': 'Petter'}]}

d["employees"].append({"firstName": "Albert", "lastName": "Bert"})
print(d)


# 56 Store the dictionary in a json file.
import json # built-in module

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("56.json", "w") as file:
    json.dump(d, file, indent=4, sort_keys=True)


# 57 Print out 56.json content
import json
from pprint import pprint # sometimes import <moduleName> alone won't work

with open("56.json", "r") as file:
    # pprint(json.load(file))       # TypeError: 'module' object is not callable
    # pprint(json.loads(file.read())) # TypeError: 'module' object is not callable
    d = json.loads(file.read())     # json.loads() gets a string as output and creates a dictionary object out of that.

pprint(d)


# 58 add a new employee to the content of "56.json"
import json

with open("56.json", "r+") as file:     # "+" write mode
    d = json.loads(file.read())         # 
    d["employees"].append({
        "firstName": "Albert",
        "lastName": "Bert"})
    file.seek(0)        # move cursor to start of file
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()     # delete everything after current cursor position (end of dumped dictionary)


