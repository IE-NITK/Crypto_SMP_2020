N=(int)(input("Enter a number : "))
num=2
last=(int)(N/2)+1
for i in range(2,last):
    if (N%i==0):
        num=num+1
print(num)



