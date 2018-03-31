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

