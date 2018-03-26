# 26 Make a script that prints out numbers from 1 to 10
# Expected output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

[print(num) for num in range(1, 11)]


# 27 Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. The formula for acceleration is: a = delta v / delta t
# To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2 respectively, and you should get the expected output.

# Expected output:
# 0.5
def accel(v1=0, v2=0, t1=0, t2=0):
    print("a = delta v / delta t\n",
    "a = (v2 -v1)/(t2 - t1)\n",
    "a = ({v2} -{v1})/({t2} - {t1})\n".format(v1=v1,v2=v2,t1=t1,t2=t2),
    "a = " + str((v2 -v1)/(t2 - t1)))
accel(0, 10, 0, 20)


# 28 Why is there an error in the code and how would you fix it?

def foo(a, b):
    # print(a + b)  # needs to return something
    return a + b

x = foo(2, 3) * 10 # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
print(x)


# 29 Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter. Liquid volume = ( (4*pi**3)/3 ) - ( pi*h**2*(3*r-h)/3 )

# You can then test your solution by passing 2 for h and you should get the expected output.
# Expected output:
# 4071.5040790523717

from math import pi
def liquid_volume(h, r=10):
    return (( 4 * pi * r**3 ) / 3) - (pi * h**2 * (3*r - h) / 3 )

print(liquid_volume(2))


# 30 Why do you get an error and how would you fix it?

# def foo(a=2, b): # SyntaxError: non-default argument follows default argument
def foo(b, a=2):
    return a + b
print(foo(5))


# 31 Why is there an error in the code and how would you fix it?

def foo(a=1, b=2):
    return a + b

x = foo() - 1 # TypeError: unsupported operand type(s) for -: 'function' and 'int'
print(x)


# 32 What will the following script output? Please try to do this mentally if you can.

c = 1 # c set to 1
def foo():
    return c
c = 3 # c set to 3
print(foo()) # => 3


# 33 Here's another similar exercise. What will the following script output? Try to do this mentally if you can.

c = 1
def foo():
    c = 2   # local c set to 2
    return c
c = 3
print(foo()) # returning foo's local c => 2


# 34 The following script throws a NameError  in the last line saying that c  is not defined. Please fix the function so that there is no error and the last line is able to print out the value of c  (i.e. 1 ).
# c = 1
def foo(): 
    # c = 1     # need to move local c to global scope
    global c    # makes c available in the global namespace
    c = 1       # need to set c, else NameError: name 'c' is not defined
    return c 
foo() 
print(c) # NameError: name 'c' is not defined
# Expected output:
# 1 
