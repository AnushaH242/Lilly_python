Name = input("Enter your name: ")

import cal
import sys


j = cal.hra()
print("Your hra: ",j)
k = cal.da()
print("Your DA: ",k)
l = cal.bonus()
print("Your Bonus: ",l)

x = int(j) + int(k) + int(l)
print("total salary: ", x)