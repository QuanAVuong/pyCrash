# 1
a = 2
a = 4
a = 6
print(a + a + a) # => 18

# 2
a = 1
_a = 2
_a2 = 3
2a = 4 # variables' names cannot start with a number

# 3
a = 1
b = 2
print(a == b) # => False
print(b == c) # => NameError: name 'c' is not defined

# 4.
a = "1"
b = 2
# print(a + b) # TypeError: must be str, not int  
print(int(a) + b) 

# 5
# Question: Complete the script so that it prints out the second item of the list.

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 

# b
print(letters[1])


# 6
# Question: Please complete the script so that it prints out a list slice containing items d , e , and f .

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 

# ['d', 'e', 'f'] 
print(letters[3:6])

# 7
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 

# ['a', 'b', 'c'] 
print(letters[:3])