for num in range(100):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
        print("FizzBuzz")
    if num % 3 == 0:
        #print(num)
        print("Fizz")
        continue
    if num % 5 == 0:
        #print(num)
        print("Buzz")
        continue
if num > 0:
    for i in range(2,num):
        creciente = 2
        esPrimo = True
        while esPrimo and creciente < i:
            if i % creciente == 0:
                esPrimo = False
            else:
                creciente +=1
        if esPrimo:
            print("Prime:",i)  

