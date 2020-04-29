#Making the list of first 26 prime numbers

def primecheck(x):
    a = [True for i in range(0,x+1)]
    b = 2
    while b*b <= x:
        if(a[b] == True):
            for c in range(b*b,x+1,b):
                a[c] = False
        b += 1
    c = []
    for i in range(2,x+1):
        if a[i]:
            c.append(i)
    return c
char = primecheck(101)

#Accepting the strings
a = list(input('Enter 1st string'))
b = list(input('Enter 2nd string'))
pro1 = 1
pro2 = 1

#Finding out the prime product of both the strings
for j in a:
    if j != ' ': 
        pro1 *= char[ord(j)- 97 ]
        
for j in b:
    if j != ' ':
        pro2 *= char[ord(j) - 97]

if pro1 == pro2:
    print('Anagram!!')
else:
    print('Not anagram !')

