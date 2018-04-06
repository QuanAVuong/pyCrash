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
