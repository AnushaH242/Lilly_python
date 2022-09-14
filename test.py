a = input("Enter your first name: ")
b = input("Enter your last name: ")
c = input("Enter your phone no: ")
d = input("Enter your Age: ")
e = input("Enter your emailID: ")
f = input("Enter your salary: ")
g = input("Enter your department name: ")
h = input("Enter your ID: ")
i = input("Enter your Manager: ")
j = input("Enter your city: ")


while int(len(a)) < 0 or a.isalpha() == False: 
       a =  input("enter your name again: ")

while int(len(b)) < 0 or b.isalpha() == False: 
       b =  input("enter your last name again: ")

while len(c) != 10 or c.isnumeric() == False:
    c = input("Enter a new no: ")

while len(d)==0 or int(d)<20 or d.isnumeric()==False:
    d = input("Enter a new age: ")

while len(e) == 0:
    e = input("Enter a new emailID: ")

while len(f) == 0 or len(f)<0 or f.isnumeric()== False:
    f = input("Enter a new salary: ")

while len(g)==0 or g.isalpha()==False:

    g = input("Enter new Department: ")

while len(h) == 0:
    h = input("Enter a new ID: ")

while len(i) == 0 or i.isalpha()==False:
    i = input("Enter a new Manager name: ")

while len(j) == 0 or j.isalpha()==False:
    j = input("Enter a new city name: ")


print("\nFirst name: ", a)
print("last name:", b)

print("phone no:", c)

print("age:", d)

print("emailID:", e)

print("salary:", f)
print("dept name: ", g)
print("ID", h)
print("Manager: ", i)
print("City: ", j)
