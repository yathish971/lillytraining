import os
import re
path="C:/Users/yathish.l@lilly.com/AppData/Local/Programs/Python/Python310/"
'''write a program to display all the files from the current directory line by
line with proper exception handling'''
try:
    print(os.listdir())
    '''write a program to display ONLY .py files'''
    for i in (os.listdir()):
        
            if(re.match(".*\.py",str(i))):
                    print(i)
except Exception as e:
      print(e)
'''write a program to display either its a file or a folder'''

print(os.path.isfile(path))
'''write a progarm to delete .txt files from the current directory'''
for i in (os.listdir()):
        if(re.match(".*\.txt",str(i))):
                os.remove(str(i))


# Print operating system name
print(os.name)

# Print if the path exists

try:
    a=os.listdir(path)
    print("path found")
    print(os.path.exists(path))
except Exception as e:
    print("Path not found")
             

# Create a directory
#os.mkdir("kannada")

# Get the absolute path
print(os.path.abspath(path))
# current working directory
print(os.getcwd())

# login name
print(os.getlogin())
# current process id
print(os.getpid())
