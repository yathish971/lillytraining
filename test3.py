from test_module_cal import *
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multi(a,b):
#     return a*b
# def div(a,b):
#     if b==0:
#         return "can not be divide by zero"

while True:
    print("\nSimple Calculator\n1.Add\n2.sub\n3.multi\n4.div\n5.exit")
    choice=int(input("Enter the Choice : "))
    num1=0
    num2=0
    if choice>=6 or choice<=0:
        print("Enter the correct choice")
        continue
    elif(choice!=5):
        num1=float(input("Enter the Number One: "))
        num2=float(input("Enter the Number Two: "))
    else:
        print("Thank You")
        break
    
    if choice ==1:
        r=add(num1,num2)
        print("The sum of ",num1," and ",num2," is ",r)
    elif choice==2:
        r=sub(num1,num2)
        print("The difference of ",num1," and ",num2," is ",r)
    elif choice==3:
        print("The product of ",num1," and",num2," is ",multi(num1,num2))
    elif choice==4:
        print("The quotient of ",num1,"and ",num2," is ",div(num1,num2))
    

    

