print("welcome to the tip calculator")

bill=float(input("what was your total bill ? "))

percentage=float(input("what percentage tip you would like to give ? 10,20, "))

Numeber_people=int(input("Enter the Number of the people"))
percentage=percentage/100
percentage+=1
split=(bill/Numeber_people)*percentage
print("each person need to pay :",split)