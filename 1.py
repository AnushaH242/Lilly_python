#details 
print("Enter your firstname")
var1 = input()
print("Enter your middle name")
var2 = input()
print("Enter your last name")
var3 = input()
x = var1,var2,var3


print("enter your DOB")
a = (input())
from datetime import date
today = date.today()


b = today.year - int(a)
print("Enter your phone")
c = input()
print("Enter your adress")
d = input()
print("Enter your pin")
e = input()
print("Enter your ID")
f = input()
print("Enter your Company")
g = input()

print("Name =",x,"DOB =",a,"AGE =", b,"PHONE=",c,"Address=",d,"PIN=",e,"id=",f,"Company=",g )


