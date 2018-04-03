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


# 59 Please complete the code so that it prints out the expected output.

a = [1, 2, 3] 

# Expected output: 
# Item 1 has index 0
# Item 2 has index 1
# Item 3 has index 2

for index, value in list(enumerate(a)) :
    print("Item %s has index %s" % (value, index))



# 60 Prints hello repeatedly, non-stop
while True:
    print("Hello")


# 61 Create a program that prints out Hello  every two seconds.

# Expected output: 
# ...
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# ...
import time

while True:
    print("Hello")
    time.sleep(2)


# 62 Create a program that once executed the program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.

# Expected output: 
# ...
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# ...
import time
timer = 0
while True:
    print("Hello")
    timer += 1
    print(timer)
    time.sleep(timer)


# 63  Create a program that once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

# Expected output: 
# Hello
# Hello
# Hello
# Hello
# End of Loop
import time
timer = 1
while timer <= 3:
    print("Printing 'Hello' after {0} {1}: Hello ".format(timer, "second" if timer <= 1 else "seconds"))
    timer += 1
    time.sleep(timer)
print("End of the Loop")



# 64 The following code prints Hello, checks if 2 is greater than 1 and then breaks the loop because 2 is actually greater than 1. Therefore Hi is not printed out. Please replace break with something else so that Hello and Hi are printed out repeatedly.
import time

while True:
    print("First statement")
    if 2 > 1:
        # break     # break out of the loop
        # pass
        "do something"
    print("Second Statement")
    time.sleep(1)


# 65 The following code prints Hello, checks if 2 is greater than 1 and then breaks the loop because 2 is actually greater than 1. Therefore Hi is not printed out. Please replace break with something else so that Hello is printed out repeatedly and Hi is never printed.
import time

while True:
    print("First statement")
    time.sleep(1)
    if 2 > 1:
        # break         # break out of the loop
        # pass          # pass on to the next line
        continue        # continue continues with the beginning of the loop, opposite of break
    print("Second Statement")


# 66 Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 
# Enter word: earth
# terra
def engToPor():
    word = input("What word from our dictionary would you like to be translated:")
    # print("{} means ".format(word) + {value for key, value in d.items() if key == word})      # => earth means {'terra'}
    { print("{} is ".format(word) + value) for key, value in d.items() if key == word }        # => earth means terra

engToPor()


# 67 Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 

# Enter word: hello
# We couldn't find that word!
def engToPor2():
    word = input("Please enter an english word to be translated to portuguese: ")
    # { print("{} is {} in Portuguese".format(word, value)) if key == word else print("We couldn't find that word!") for key, value in d.items() if key == word }     # else clause won't run as key == word already always true
    # { print("{} is {} in Portuguese".format(word, value)) if key == word else print("We couldn't find that word!") for key, value in d.items()}     # => will run true/false statements for ALL key,value pairs

    # non-comprehension / ternary cleaner
    print(f"{word} is {d[word]} in Portuguese" if word in d else raise ValidationError(f"{word} not found."))       # => invalid syntax raise raises an exception which is a statement, not an expression that returns a value
    print(f"{word} is {d[word]} in Portuguese" if word in d else "Error: not found.")
engToPor2()


# 68 Also, make the program non case-sensitive meaning that for example, both earth and Earth should return the translation correctly for that word.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 
# Enter word: hello
# We couldn't find that word!

def engToPor3():
    word = input("Enter English word (case-insensitive): ").lower()
    print(f"{word} is {d[word]} in Portuguese" if word in d else "Error: not found.")

engToPor3()


# 69 Create an empty file. Paste the following code in the file (manually):

import requests

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])
# Executing the script will throw an error. Please fix that error so that you get the expected output and explain why the error happened.

# Expected output: 
# <!DOCTYPE html>
# <!--[if IE 7]>
# <html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">


# 70 
# Print out the text of this file http://www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.
# Expected output: 
# Distant regions of space are assumed to exist and to be part of reality as much as we are, even though we can never
# interact with them... Typically, the observable universe is taken to mean the portion of the Universe that
# is observable from our vantage point in the Milky Way.
import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
print(response.text)


# 71 Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

# Expected output: 
# 47

import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
# a_count = []
# [ a_count.append(letter) for letter in response.text if letter == "a" ]
# print(len(a_count))
print(response.text.count("a"))     # using str.count()