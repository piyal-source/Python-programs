#0.02s 9188KB
pr=[10,5,15,7,6,18,3]
wt=[2,3,5,7,1,4,1]
n,m=7,15
rem=m
x=[]
p=[]
w=[]
sum=0
for i in range(n):
    x.append(0)
pw=[]
for i in range(n):
    pw.append(pr[i]/wt[i])
for i in range(n):
    mx=pw.index(max(pw))
    p.append(pr[mx])
    w.append(wt[mx])
    pw[mx]=0
for i in range(n):
    if rem-w[i]>=0:
        sum+=p[i]
        rem-=w[i]
        x[i]=1
    else:
        sum=sum+(p[i]*rem/w[i])
        x[i]=round(rem/w[i],2)
        rem=0
        break
print(x)
print(round(sum,2))