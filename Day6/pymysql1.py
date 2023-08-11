import pymysql
mydb=pymysql.connect(host="127.0.0.1",user="root",password="Jyothi8762@")
print(mydb)
mycursor=mydb.cursor()
sql_statments =["create database lilly;","use lilly;","create table emp(id int,name varchar(50),designation varchar(50));","insert into emp values(1,'yathish','analyst');","select * from emp;"]
for statment in sql_statments:
    mycursor.execute(statment)
    mydb.commit()
#mycursor.execute("create database lilly")
mycursor.close()
mydb.commit()
mydb.close()