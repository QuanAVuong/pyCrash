# 76 Make script that prints out the current day, and time. For example Today is Sunday, December 25, 2016 .
from datetime import datetime       # The datetime (from datetime) module supplies classes (import datetime) for manipulating dates and times 

# datetime.datetime.now(): classmethod datetime.now(tz=None) Return the current local date and time. 
# datetime.datetime.strftime(format): Return a string representing the date and time, controlled by an explicit format string. 
print(datetime.now().strftime("Today is %A, %B %d %Y"))

# from mypackage.mymodule import myclass        # mypackage/[__init__.py, mymodule.py] >> myclass
# datetime — Basic date and time types. Source code: Lib/datetime.py
# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
import datetime     # => AttributeError: module 'datetime' has no attribute 'now'
import datetime.datetime      # => ModuleNotFoundError: No module named 'datetime.datetime'; 'datetime' is not a package
# from datetime import datetime

# print(datetime.now())
print(datetime.datetime.now())



# 77 Create a script that asks the user to enter their age and the script calculates the user's year of birth and prints it out in a string like in the expected output. Please make sure you generate the current year dynamically.

# Expected output: 
# You were born back in 1988
from datetime import datetime

age = int(input("Please enter your age: "))
yob = datetime.now().year - age
print(f"You were born around {yob}")


#  78 Create a program that generates a password of 6 random alphanumeric characters / words.
# random — Generate pseudo-random numbers
# Source code: Lib/random.py
# This module implements pseudo-random number generators for various distributions.
import random 

population = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
population2 = ["mot", "ghost", "rand", "leap", "born", "roll", "!@#$%^&*()?", "United", "toilet", "tea", "cheese"]
# random.sample(population, k): Return a k length list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.
sample = random.sample(population2, 6)
password = " ".join(sample)
print(password)


# 79 Create a program asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter and at least 5 characters. If the conditions are generated, print out "Password is fine", otherwise keep prompting the user for a password.

conditionsMet = False

while conditionsMet != True:
  password = input("Entered password must contain >= 1 number, 1 uppercase, >= 8 char:\n")
  
  if all( char.isdigit() == False for char in password ):
    print("Does not meet the number condition")
  elif all(char.isupper() == False for char in password):
    print("Does not meet the uppercase condition")
  elif len(password) < 5:
    print("Does not meet the length condition")
  else:
    print("Your password passed the security check")
    conditionsMet = True



# 80 Create a program asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter and at least 5 characters. If the conditions are generated, print out the reason why pointing to the specific condition/s that has not been satisfied.
while True:
  errors = []
  password = input("Entered password must contain >= 1 number, 1 uppercase, >= 8 char:\n")
  
  if all( char.isdigit() == False for char in password ):
    errors.append("No numbers.")
  if not any(char.isupper() == True for char in password):
    errors.append("No upppercase letters.")
  if len(password) < 8:
    errors.append("Less than 8 characters")
  if len(errors) == 0:
    print("Your password passed the security check")
    break
  else:
    # print(f"Errors found: {len(errors)}")
    [print(f"Error {index+1}: {value}") for index, value in enumerate(errors)]



# 81 Ask users to create an account with a username and password. If username already exists in 81-users.txt, create a new one.
while True:
	username = input("Please choose a non-existing username: ")
	with open("81-users.txt", "r") as file:
	  lUsers = file.read().splitlines()
	if username not in lUsers:
		break
	else:
		print("Entered username already exists.")

while True:
	errors = []
	password = input("\nPlease create a valid password.\nEntered password must contain >= 1 number, 1 uppercase, >= 8 char: ")

	if all( char.isdigit() == False for char in password ):
		errors.append("No numbers.")
	if not any(char.isupper() == True for char in password):
		errors.append("No upppercase letters.")
	if len(password) < 8:
		errors.append("Less than 8 characters")
	if len(errors) == 0:
		print(f"\nYour new username and password is:\nusername: {username}\npassword: {password}")
		break
	else:
		[print(f"Error {index+1}: {value}") for index, value in enumerate(errors)]