m = "Anusha"
a1 = 4
a = "this is %s %s"%(m,a1)
print(a)

c = "this is {} {}"
b = c.format(m,a1)
print (b)

d = f"This is {m} {a1}"
e = f"this is {m} {a1} {4*5}"
print(d)
print(e)
