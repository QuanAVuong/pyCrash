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


# 82 Use Python to calculate the distance in kilometers between Jupiter and Sun on January 1, 1230. 

# Expected output: 
# 758085657.5026425

# ephem 3.7.6.0: Compute positions of the planets and stars
import ephem 
jupiter = ephem.Jupiter()
jupiter.compute("1230/1/1")
distance_in_au = jupiter.sun_distance
distance_in_km = distance_in_au * 149597870.691
print(distance_in_km)


# 83 Write a script that detects and prints out your monitor resolution.

# Expected output: 
# Width: 1920,  Height: 1080
from screeninfo import get_monitors

print(f"You have {len(get_monitors())} monitors with the following resolutions:\n",
			f"monitor 1: {get_monitors()[0].width} width x {get_monitors()[0].height} height\n",
			f"monitor 2: {get_monitors()[1].width} width x {get_monitors()[1].height} height ")


# 84 Create a Helo World GUI
# pyglet provides an object-oriented programming interface for developing games and other visually-rich applications for Windows, Mac OS X and Linux.
# http://pythonhosted.org/pyglet/programming_guide/index.html
# pip install --force-reintstall pyglet==1.4.0a1
import pyglet
window = pyglet.window.Window()		# Create a Window by calling its default constructor. 
label = pyglet.text.Label("Hello World",				# To display the text, we'll create a Label.
				font_name="Helvetica",									# Keyword arguments are used to set the font
				font_size=72,														 
				x=window.width//2, y=window.height//2,	# position
				anchor_x="center", anchor_y="center")		# and anchorage of the label

# An on_draw event is dispatched to the window to give it a chance to redraw its contents.
# pyglet provides several ways to attach event handlers to objects; a simple way is to use a decorator:
# https://stackoverflow.com/questions/6392739/what-does-the-at-symbol-do-in-python
@window.event
def on_draw():		# basically on_draw will be passed to window.event: on_draw() = window.event( on_draw )
	window.clear()
	label.draw()

pyglet.app.run()



# 85 The file 85-countries-raw.txt contains the list of country names, but it also contains some unnecessary text among the countries. 
# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or break lines in it. The new file content should look like in the expected output.

# Expected output: 
# Afghanistan
# Albania
# Algeria
# ...

with open("85-countries-raw.txt", "r") as file:
	lCountries = file.readlines()

lCountries = [ i.strip("\n") for i in lCountries if "\n" in i ]		# removing all '\n' instances
lCountries = [ i for i in lCountries if i != "" ]		# removing empty strings
lCountries = [ i for i in lCountries if i != "Top of Page" ]		# removing "Top of Page" instances
lCountries = [ i for i in lCountries if len(i) != 1 ]		# removing alphabetical section eg A, B, C instances

with open("85-countries-clean.txt", "w") as file:
	for i in lCountries:
		file.write( i + "\n" )



# 86 Please take a look at the following list:
# One of the items is not a country. Please use Python and 85-countries-clean.txt as data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.

checklist = ["Portugal", "Germany", "Munster", "Spain", "Saint Lucia", "Yemengg", "Bulgarian"]

# Expected output: 
# ['Portugal', 'Germany', 'Spain', 'Saint Lucia']

with open("85-countries-clean.txt", "r") as file:
	lCountries = file.readlines()
	lCountries_clean = [ country.rstrip("\n") for country in lCountries ]
	filtered = [ i for i in checklist if i in lCountries_clean ]
	print(filtered)


# 87 Add the missing item to the file
checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]

with open("87-missing.txt", "r") as file:
  lMissing = file.readlines()

lFixed = sorted(checklist + lMissing)

with open("87-fixed.txt", "w") as file:
  for i in lFixed:
    file.write(i)
