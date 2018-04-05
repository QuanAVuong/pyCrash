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
