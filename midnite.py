score=0
a=input("what is the name of the owner of this system")
if a=="Ekere Ifechukwu Dominic":

    print("CORRECT")
    score += 1
else:


    print("WRONG")
b=input("What is his best food")
if b=="he does not have one" or "he no get":
    print("CORRECT")
    score += 1
else:
    print("WRONG")
c=input("does he have a best friend")
if c=="yes":

    print("CORRECT")
    score += 1
else:


  print("WRONG")
d=input("where is his dream city")
if d=="Paris" or "New York  ":

    print("CORRECT")
    score += 1
else:

   print("WRONG")
e=input("what is his favorite subject")
if e=="chemistry":

    print("CORRECT")
    score += 1
else:


   print("WRONG")
if score==5:
  print("""you got """ ,score,"""/""",5,"""
  WOW! YOU GOT EVERYTHING YOU REALLY KNOW THIS GUY""")
else:
    print("""you got """ ,score,"""/""",5,"""
    go and try to learn more about ur friend""")