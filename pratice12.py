Pizza_size=int(input("Enter the Pizza Size \n 1 for Small Pizza \n 2 for Medium Pizza \n 3 for Large Pizza\n"))
total=0
if Pizza_size<=3 or Pizza_size<=0:
   pass
else:
    print("enter the Correct Pizza size")

Pepperoni_c=int(input("Press 1 For Pepperoni \nPress 0 For skip\n"))
cheese=int(input("Press 1 for Extra Cheese \nPress 0 For skip Extra Cheese\n"))

print("***********************************************************************")
print("Bill Details ")
print("***********************************************************************")
if(Pizza_size==1):
    total=15
    print("Pizza size is Small : 15" )
    if(Pepperoni_c==1):
        total+=2
        print("Peeperoni : 2" )
    
    if cheese==1:
        print("Cheese : 1" )
        total+=1
    print("Total Bill is : ",total)
if(Pizza_size==2):
    total=20
    print("Pizza size is Small : 20" )
    if(Pepperoni_c==1):
        total+=3
        print("Peeperoni : 3" )
    if cheese==1:
        total+=1
        print("Cheese : 1" )
    print("Total Bill is : ",total)
if(Pizza_size==3):
    total=25
    if(Pepperoni_c==1):
        total+=3
        print("Peeperoni : 3" )
    if cheese==1:
        total+=1
        print("Cheese : 1" )
    print("Total Bill is : ",total)

    
    