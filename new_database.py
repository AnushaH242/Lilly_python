import mariadb 
import sys
conn = mariadb.connect(
    user = 'root',
    password = 'vashisector15',
    host = 'localhost',
    port = 3306,
    database= 'python'
    )

x = conn.cursor()
conn.autocommit = True


try:
    x.execute('CREATE TABLE details (first_name VARCHAR(30),last_name VARCHAR(50), phone_no int(30), age int(20), email_ID varchar(30), salary int(100), department_name varchar(255), ID int(30), Manager varchar(50),city varchar(20))')
except Exception as y:
    print(y)    

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
phone = input("Enter your phone no: ")
age = input("Enter your Age: ")
email = input("Enter your emailID: ")
sal = input("Enter your salary: ")
depart = input("Enter your department name: ")
id = input("Enter your ID: ")
manager = input("Enter your Manager: ")
city = input("Enter your city: ")


a = ('INSERT INTO details(first_name, last_name, phone_no, age, email_ID, salary,department_name, ID, Manager, city) VALUES (%s,%s,%d,%d,%s,%d,%s,%d,%s,%s)')
b = (fname, lname, int(phone), int(age), email, int(sal),depart,int(id), manager, city)
x.execute(a,b)
x.execute('SELECT * from details;')

for (fname, lname, phone, age, email, sal,depart,id, manager, city) in x:
    print(fname, lname, phone, age, email, sal,depart,id, manager, city)
x.close()