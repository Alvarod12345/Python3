"""
Homework11
Error Handling
ASL
"""

def OnlyInteger(a=None,b=None):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Error:")
        print("Got a value error. Only Integers")
    except Exception as  e:
        print("Error:")
        print(e)
    finally:
        print("Values",a,b)
    
def file(a):
    try:
        a = open(a)
    except FileNotFoundError as e:
        print("Error:")
        print(e)
    except Exception as e:
        print("Error:")
        print(e)
    else:
        print(a.read())
        a.close()
    finally:
        print("Finally..")

OnlyInteger("hello","world")
print("\n")
OnlyInteger(True,False)
print("\n")
OnlyInteger([1],[2])
print("\n")
OnlyInteger(1.1,1.2)

file("example.txt")
print("\n")
file("example1.txt")
print("\n")
file([2])
print("\n")
file([True])