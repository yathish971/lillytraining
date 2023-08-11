#String Functions 
name="thinknyx "

print("The First Character ",name[0])
len_name=len(name)
print("The Last Character ",name[len_name-1])
print("the Upper case",name.upper())
print("The Number of 'n' is repeats ",name.count("n"))
print("The Capitalized :",name.capitalize())
print("in" in name)
print(name.startswith("t"))
print("after reaplacing",name.replace("thinknyx","thinknyxtechnologies"))
print("after removing space",name.replace(" ",""))
print("after removing the space",name.lstrip())