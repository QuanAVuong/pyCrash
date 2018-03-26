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

# 8 Question: Complete the script so that it prints out letter i  using negative indexing.

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 

# i 
print(letters[-2])

# 9 Question: Complete the script so that it prints out a list slice containing the last three items of list letters .

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output:

# ['h', 'i', 'j'] 
print(letters[-3:])

# 10 Question: Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 
# 2 points
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Expected output: 

# ['a', 'c', 'e', 'g', 'i'] 
print(letters[0::2])

# 11 Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.
print(list(range(1, 21)))

# 12 Complete the script so that it produces the expected output. Please use my_range  as input data.

my_range = range(1, 21)
#  Expected output: 

# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] 
print([10 * num for num in my_range ])


# 13 Complete the script so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.

my_range = range(1, 21)
#  Expected output: 

# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']  
print([str(num) for num in my_range]) # list comprehension
print(list(map(str, my_range))) # map function


# 14 Complete the script so that it removes duplicate items from list a .

# Expected output: 
#   ['1', 2, 1] 

from collections import OrderedDict # 2.1 preserving order
a = ["1", 1, "1", 2]

print("This list made from a set is unique but does not preserve order: " + str(list(set(a)))) # 1. order not preserved
print("Preserving order with OrderedDict.fromkeys(a): " + str(list(OrderedDict.fromkeys(a)))) # 2.1

# 2.2 Preserve order by appending another list:
b = []
for elem in a:
    if elem not in b:
        b.append(elem)
print("Regular for => if => append" + str(b))

b = []
list(map(lambda elem: b.append(elem) if elem not in b else False, a ))
print("ternary lambda: " + str(b)) # => [None, None, False, None]

# the operation b.extend (from b.extend([elem for elem in a if elem not in b])) happens after generating the list from list-comprehention, while that specific b.append (from [b.append(elem) for elem in a if elem not in b])  is activelly appending to b while checking if it already contains something from a, and not appending it if it does
b = []
b.extend([elem for elem in a if elem not in b]) # => ['1', 1, '1', 2]
print("extend() makes a copy: " + str(b))

b = []
[b.append(elem) for elem in a if elem not in b]
print("List comprehension: [append.. for.. if..]" + str(b))


# 15 Create a dictionary that contains the keys a  and b  and their respective values 1  and 2 .
d1 = {"a": 1, "b": 2}
d2 = dict(a=1, b=2)
print(d1, d2)


# 16 Please complete the script so that it prints out the value of key b .

d = {"a": 1, "b": 2}
# Expected output: 
# 2  

print(d["b"])


# 17 Calculate the sum of the values of keys a  and b .

d = {"a": 1, "b": 2, "c": 3}
# Expected output: 
# 3  

print(d["a"] + d["b"])


# 18 
d = {"Name": "John", "Surname": "Smith"}
# print(d["Smith"]) # => KeyError: 'Smith'
print(d["Surname"])


# 19 Add a new pair of key (e.g. c ) and value (e.g. 3 ) to the dictionary and print out the new dictionary.

d = {"a": 1, "b": 2}
# Expected output: 
#   {'a': 1, 'c': 3, 'b': 2} 

d["c"] = 3
print(d)


# 20 Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}
# Expected output: 
#  6 
s = 0
for num in list(d.values()):
    s += num
print(s)

#d.values()  returns a list-like dict_values  object while the sum  function calculates the sum of the dict_values  items.
print(sum(d.values()))


# 21 Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
# Expected output: 
# {'a': 1}  
print(dict((key, value) for key, value in d.items() if value <= 1))
print({key: value for key, value in d.items() if value <= 1})
print({key: d[key] for key in d if d[key] <= 1}) # without items()


# 22 Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30 respectively. Then print out the dictionary in a nice format.
d = {"a": list(range(1, 11)),
    "b": list(range(11, 21)),
    "c": list(range(21, 31))}
print(d)
# use dict() and pprint
from pprint import pprint
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(d)


# 23  Access the third value of key b  from the dictionary.

from pprint import pprint
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# Expected output: 
# 13  

print(d["b"][2])


# 24 Please complete the script so that it prints out the expected output.
# Expected output: 
# b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from pprint import pprint
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# for key in d:
#     pprint(key + " has value " + str(d[key]))
# pprint(d)

# dict(print(key + " has value " + str(value)) for key, value in d.items()) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
{pprint(key + " has value " + str(value)) for key, value in d.items()} # with items()
{print(key, " has value ", str(d[key])) for key in d} # without items(), "+""


# 25 Make a script that prints out letters of English alphabet from a to z, one letter per line in the terminal.
import string
[ print(char) for char in string.ascii_lowercase ]


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