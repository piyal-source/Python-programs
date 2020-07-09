n = 12
a = [_ for _ in range(2,n+1)]
v = [0]*(n-1)

p = 0
while True:
    for i in range(a[p]*a[p],n+1):
        if i % a[p] == 0:
            v[a.index(i)] = 1
    if v[p+1:n+1].count(0)==0:
        break
    else:
        p = v.index(0,p+1,n-1)
# print(f'{a}\n{v}\n')
for i in range(n-1):
    if v[i]==0:
        print(a[i], end=" ")