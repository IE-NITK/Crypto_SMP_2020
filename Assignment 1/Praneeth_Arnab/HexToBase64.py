d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
e="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
s=input("Enter the string\n")
n=len(s)
s=list(s)
l=0
for i in range(n):
        l=l+d[s[i]]*(16**(n-i-1))
t=''
while l!=0:
        m=l%64
        l=l//64
        t=e[m]+t
print(t)
