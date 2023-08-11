name=input("Enter Your Name")
Age=int(input("Enter the age"))
country=input("Enter the Country")
is_eligible=False

if Age >= 18:
    if country=="india":
        is_eligible=True
print(name," is Eligible ",is_eligible)