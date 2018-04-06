# 1 Find the probabilities of the following rocks rounded to the nearest hundredth:
rocks = {
  "sedimentary": 58,
  "metamorphic": 213,
  "igneous": 522,
}
# Expected ouput:
#  There is 0.07 probability of the sedimentary rock 
#  There is 0.27 probability of the metamorphic rock 
#  There is 0.66 probability of the igneous rock 

[ print(f" There is {round( value / sum(rocks.values() ), 2)} probability of the {key} rock ")
    for key, value in rocks.items() ]


# 2 X is a discrete random variable. The table below defines a probability distribution for X. What is the expected value of X?

x = [10, 20, 30, 40]
p = [.2, .3, .15, .35]
e = 0

for x, p in zip(x, p):
    print(f"{x} * {p} = {x*p} + ")
    e += x*p     
print(f"Expected Value: {e}")