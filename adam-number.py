a=int(input())
sq=a*a#144
d=0
d1=0
sum=0
rev=0
while(a>0):
    d=a%10
    sum=sum*10+d
    a=a//10
sq1=sum*sum
while(sq1>0):
    d1=sq1%10
    rev=rev*10+d1
    sq1=sq1//10
if(sq==rev):
    print("True")
else:
    print("False")
