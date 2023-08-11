N=input("Enter the N Number: ")
for i in range(1,int(N)+1):
    if i%3==0 and i%5==0:
        print("Bizz Buzz")
    else:
        if i%3==0:
            print("Bizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)