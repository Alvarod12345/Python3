"""
Class While
While structure
while(condition)
    Action1
    Action2
"""
counter = 1
sum = 0
while(counter<=10):
    sum +=counter
    # print(counter)
    counter += 1
# print(sum)

Letters = ["a","b","c","d","e","f"]
index = 0
while(index < len(Letters)):
    # print(index)
    # print(Letters[index])
    index+=1

height = 5000
velocity = 50
time = 0
while(height>0):
    height = height - velocity
    time +=1
    
print(height)
print(time)