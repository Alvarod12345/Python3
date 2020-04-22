# Error Handling

keyword = "helloworld"

# ex1
# try:
#     print(int(keyword))
# except:
#     print("got a value error")


# ex2 using exception
# try:
#     print(int(keyword))

# except Exception as e:
#     print(e)

# ex3
# try:
#     print(int(keyword))
# except ValueError:
#     print("got a value error")
# except:
#     print("other except")
# finally:
#     print("finally")


# ex4
try:
    # raise ValueError
    # raise ZeroDivisionError
    # raise AttributeError
    raise NameError("Error 1")

except ValueError:
    print("you got a value error")
except ZeroDivisionError:
    print("zero division error")
except AttributeError:
    print("you got a atribute error")

except Exception as x:
    print("except")
    print(str(x))
finally:
    print("finally")


