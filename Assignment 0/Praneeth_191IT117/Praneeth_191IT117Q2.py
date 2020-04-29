x=int(input("Enter the number\n"))
i=1
n=0
while i*i<=x:
        if x%i==0:
                n=n+1
                if x//i!=i:
                        n=n+1
        i=i+1
print(n)
