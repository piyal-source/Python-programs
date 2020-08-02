t=2
for i in range(2):
    st=input()
    rs=st[len(st)-1::-1]
    print(rs)
    #OR
    re=''
    for j in range(len(rs)-1,-1,-1):
        re+=rs[j]
    print(re)