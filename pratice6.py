#format function 
sentence ="I like {}  and  {}"
print(sentence.format("C#","JAVA"))
# split function
sentence_split="yathish,rahul,ramesh,vinay"
print(sentence_split.split(","))
#challange 

print("{} and {}".format("192.168.0.1","192.168.0.2"))

name =input("Enter the Input")
length = len(name)
length=length*2
name=list(name)
for i in range(1,length-1,2):
    name.insert(i,"-")
changed_name=""
for x in name:
    
    changed_name=changed_name+str(x)
print(changed_name)