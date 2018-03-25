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

