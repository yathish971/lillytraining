import random as r 

z=r.randint(1,2)
if z==1:
    print("Head")
else:
    print("Tail")

#or 
print(r.choice(["Heads","Tails"]))