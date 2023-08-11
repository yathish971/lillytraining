
marks=(20,35,42,49,26)
sum=0
for i in marks:
    sum+=i
avg=sum/len(marks)
print("The Avreage is ",avg)
print("Thre First marks",min(marks))
print("The last Marks",max(marks))
print("The central number is ",marks[(len(marks)//2)])