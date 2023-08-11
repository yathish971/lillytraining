import mysql.connector
import pymysql

# mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="Jyothi8762@")
# print(mydb)
# mycursor=mydb.cursor()
# sql_statments =["create database lilly;","use lilly;","create table emp(id int,name varchar(50),designation varchar(50));","insert into emp values(1,'yathish','analyst');","select * from emp;"]
# for statment in sql_statments:
#     mycursor.execute(statment)
#     mydb.commit()
# #mycursor.execute("create database lilly")
# mycursor.close()
# mydb.commit()
# mydb.close()



# 
# for i in sql_statments:
#     print(i)
#     try:
#         mycursor.execute(i)
#     except Exception as e:
#         print(e)



def connect(db_host,db_user,db_password,db_database):
    con= pymysql.connect(host=db_host,user=db_user,password=db_password,database=db_database)
    return con

def insert(id,name,email):
    query="insert into emp values({},'{}','{}')"
    query=query.format(id,name,email)
    #print(query)
    con=connect("localhost","root","Jyothi8762@","lilly")
    cursor=con.cursor()
    cursor.execute(query)
    cursor.close()
    con.commit()
    con.close()
    

def display():
    query="select * from emp"
    con=connect("127.0.0.1","root","Jyothi8762@","lilly")
    cursor=con.cursor()
    cursor.execute(query)
    for i in cursor:
        print(i)



while True:
    print("Press 1 for insert \npress 2 for display \npress 3 for Exit")
    ch = int(input("Enter the Choice : "))
    if ch==1:
        id=int(input("Enter the Id: "))
        name=input("Enter Name of the Employee Name : ")
        email=input("Enter the Designation : ")
        insert(id,name,email)
    elif ch==2:
        display()
    elif ch==3:
        break
    else:
        print("Enter the Correct Choice")