print("enter first value:")
a = input()
print("enter second value")
b = input()
try: 
    print("The addition of the values:", int(a) + int(b))
except Exception as y:
    print(y)
print("this code is good")