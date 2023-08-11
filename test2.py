# def primeornot(Number):
#     flag=True
#     for i in range(2,int(Number**0.5)+1):
        
#         if Number%i==0:
#             print(Number,"Not a Prime Number")
#             flag=False
#             break
#     if flag:
#         print(Number,"prime Number")

# #Number = int(input("Enter the Number "))
# for i in range(1,100):
#     primeornot(i)



def check1(a):
    if a%2==0:
        return True
    else:
        return False
    
print(check1(10))