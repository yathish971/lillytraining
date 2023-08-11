while True:
    
    Height=int(input("Enter the  height in CM : "))

    if Height > 120:
        Age = int(input("Enter the age : "))
        
        if Age<12 and Age>1:
            print("Can Ride")
            print("Price is 50")
        elif Age<18 and Age>=12:
            print("Can Ride")
            print("Price is 100")
        elif Age>=18 and Age <=80:
            print("Can Ride")
            print("Price is 150")
        else:
            print("Enter the Valid Age")
    else:
        print("Can't Ride")
    Check=int(input("Enter 1 to continue \nEnter 2 to Stop\n"))
    if Check==2:
        break