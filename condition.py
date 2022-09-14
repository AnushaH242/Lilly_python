"""
#largest
print("enter first value")
a = input()
print("enter second value")
b = input()
print("enter third value")
c = input()
if (a>b) and (a>c):
    print("a is largest")
elif b>a and b>c:
     print("b is largest")
else:
    print("c is the largest")

#2nd - 

total = 50
print("enter number of classes attended")
a = input()
p = int(a) *100/total
if p > 45:
    print('student is eligible')

else: 
    print('student is not eligible')
"""
#question -employee bonus

print("enter salary")
a = int(input())
print("enter the no of years worked")
b = int(input())
if b >10: 
    c = 15*salary/100
    