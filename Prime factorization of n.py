def pfactors(n):
    a = [_ for _ in range(2,n+1)]
    for i in range(n-2):
        for j in range(i+1,n-1):
            if a[j]%a[i]==0 and a[j]>a[i]:
                a[j]=a[i]
    factors=[]
    while n!=1:
        factors.append(a[n - 2])
        n = n// a[n-2]
    return factors

print(pfactors(12))
