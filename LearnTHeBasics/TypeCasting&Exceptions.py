# <---Type Casting--->
a=int(3.14)
print(a,type(a))


# <---Exceptions--->
x=int(input("Enter value <5->"))
if x<5:
    raise Exception("Value must be greater than 5, your value was",x)

while True:
    try:
        x=int(input("Enter a value->"))
    except:
        print("Value must be an integer")
        break
    finally:
        print("Last integer entered",x)