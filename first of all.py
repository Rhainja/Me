def add(x,y):
    return x+y
def subtrac(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("""Welcome to ekere's calculator
pick out of the following functions
1.add
2.subtract
3.multiply1
4.divide""")
choice=input("Enter your choice(1/2/3/4)")
if choice in ['1','2','3','4']:
      x=float(input("enter your first number"))
      y=float(input("enter your second number"))
      if choice=='1':
        print("your answer is",add(x,y))
      elif choice=='2':
          print("your answer is",subtrac(x,y))
      elif choice=='3':
          print("your answer is",multiply(x,y))
      elif choice=='4':
          print("your answer is",divide(x,y))
      else:
          print("get out of here")
else:
    print("get outta here")