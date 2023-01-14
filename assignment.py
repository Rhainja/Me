def km_to_mile():
    x=float(input('ur km'))
    print("ur ansa in mile is",x/1.6034,"miles")
def mile_to_km():
    y=float(input('ur mile'))
    print("ur ansa in km is",y*1.6034,"km")

km_to_mile()
mile_to_km()


print("This is a funny game so enjoy")
length=int(input("Enter the value of your length: "))
breadth=int(input("Enter the value for your breadth: "))
Area=length*breadth
print("The area of your rectangle is ",Area)

try:
    first_number=int(input("Enter your value: "))
    second_number=int(input("Enter your second value: "))
    value=first_number*second_number
except ValueError:
    print("Sorry dear you need to enter an integer before I can run")

try:
    no_1=int(input("Enter a value: "))
    no_2=int(input("Ente another value: "))
    value2=no_1/no_2
    print(value2)
except BaseException:
    print("Try again later with another denominator")

try:
    y="ffffffffffff"/45
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!!")
except:
    print("Oh dear something went wrong")

print("THE END!!")
import math
def volume():
    radius=int(input('Enter your radius'))
    volume=(3/4)*math.pi*pow(radius,3)
    return volume
try:
    print(volume())
except ValueError:
    print('What happened')
    raise
except ArithmeticError:
    print('What is that')
    raise

print("THE END")


import math
try:
    x=float(input("Enter your number"))
    assert x>=0.0
    x=math.sqrt(x)
    print(x)
except AssertionError:
    print("Brosin u made a mistake")