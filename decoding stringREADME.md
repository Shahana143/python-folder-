# python-folder-
for _ in range(int(input())):
    n,d=map(int,input().split())
    st=input()
    par=+1
    if d%2==1:
        par=-1
    s=""
    j=d//2
    for i in range(d):
        j+=par*i
        s+=st[j]
        par=-(par)
    try:
        print(s+st[d:])
    except:
        print(s)
