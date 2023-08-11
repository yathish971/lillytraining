import sqlite3

conn=sqlite3.connect(r'C:\Users\yathish.l@lilly.com\OneDrive - Eli Lilly and Company\Training-python\Day6\lilly')
cursor=conn.cursor()
cursor.execute("select * from employee_info")

for i in cursor.fetchall():
    print("**************************************")
    print("Id :",i[0])
    print("Name :",i[1])
    print("desgination :",i[2])
    print("**************************************")