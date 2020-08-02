a=[7,8,5,2,4,6,3]
#  0 1 2 3 4 5 6
for i in range(1,len(a)):
    temp=a[i]
    j=i-1
    while a[j]>temp and j>=0:
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp
print(a)