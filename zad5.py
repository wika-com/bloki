a=[6,2,7,1,5]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            pomc=a[j]
            a[j]=a[j+1]
            a[j+1]=pomc
        print(a)
