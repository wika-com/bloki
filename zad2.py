maks=0
a=[]
for i in range(10):
    x=int(input("podaj x"))
    a.append(x)
print(a)
a.reverse()
print(a)
for i in a:
    if i>maks:
        maks=i
print(maks)