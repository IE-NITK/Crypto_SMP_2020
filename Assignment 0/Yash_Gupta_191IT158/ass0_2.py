import math
n=int(input())
c=0
x=math.sqrt(n)-math.floor(math.sqrt(n))
for i in range(1,math.floor(math.sqrt(n))):
    if n%i==0:
        c=c+1
c=c*2   
if n%math.floor(math.sqrt(n))==0:
    if x==0:
        c=c+1
    else:
        c=c+2
print(c)