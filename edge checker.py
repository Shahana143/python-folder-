n=list(map(int,input().split()))
if n[0]-n[1]==1or n[1]-n[0]==1:
    print("Yes")
elif n[0]-n[1]==9or n[1]-n[0]==9:
    print("Yes")
else:
    print("No")
