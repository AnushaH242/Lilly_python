
x = input("Enter your first name: ")
y = input("Enter your last name: ")

for i in x,y: 
    if len(i) == 0:
        print("Please enter a valid name")
    else: 
        print(f"NAME : {x} {y}")
    break 

a = input("Enter phone no:")
for j in a: 
    if len(a) != 10:
        print("invalid no")
    else: 
        print("Phone no:",a)
    break

b = int(input("enter age: "))
if b < 20:
    print("Invalid")
else:
    print("Your Age is: ",b)

c = input("Enter your address: ")
d = input("Enter your ID: ")

print("Your address:", c)
print("Your ID:", d))



