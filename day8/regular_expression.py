import re 


# pattern="^[89].[0-9]{9}"
# text = input("Enter the mobile number ")

# result=re.search(pattern,text)

# print(result)


# pattern="^[A-Z][a-z]*[0-9]{1}[a-z]+"
# text = input("Enter the text ")

# result=re.search(pattern,text)

# print(result)


# pattern="^[A-Z,0-9,a-z,\._\-]+@[A-Z,0-9,a-z]+\.[A-Z,a-z]{2,3}"
# text = input("Enter the email ")

# result=re.search(pattern,text)

# print(result)

email_list=["yathish971@gmail.com","Rahul@lilly.com","bharath@gmail.com"]
text="yathish971@gmail.com"
pattern2=r'(?<=.).(?=.*@)'
pattern='[^@]+'
result_main=re.search(pattern2,text)



result=re.sub(pattern2,"x",text)

print(result)