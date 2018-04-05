# 76 Make script that prints out the current day, and time. For example Today is Sunday, December 25, 2016 .
from datetime import datetime       # The datetime module supplies classes for manipulating dates and times 

# datetime.datetime.now(): classmethod datetime.now(tz=None) Return the current local date and time. 
# datetime.datetime.strftime(format): Return a string representing the date and time, controlled by an explicit format string. 
print(datetime.now().strftime("Today is %A, %B %d %Y"))
