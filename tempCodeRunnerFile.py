
age = input("What's your age? ")
# age_last_year = age - 1         # TypeError: unsupported operand type(s) for -: 'str' and 'int'
age_last_year = int(age) - 1         
print("Last year you were %s." % age_last_year)