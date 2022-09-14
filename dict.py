d1 = {"t1":"hi", "t2":"hello","t3":"bye"}
print("Enter the key")
a = input()
print(d1[a])

d1['t4']='yo'
print(d1)
del d1['t4']

print(d1)

d1.update({'t5':'the'})
print(d1)

