# class import
import random as r # random como "r"
# from random import randint, random, uniform

# random.seed(1)
# randInt = r.randint(1,10)
# print(randInt)

# randomFloat = r.random() # random de 0 -> 0.1 all float
# print(randomFloat)

# randomUniform = r.uniform(1,10) # random de 1 -> 10 all float
# print(randomUniform)

simpleList = [1,2,3,4,5,6,7,8,9]
pickOne = r.choice(simpleList)
print(pickOne)

print(simpleList)
r.shuffle(simpleList)
print(simpleList)