import math
#To check Prime number
primes=[]
def is_prime(x):
    global primes
    for divisor in primes:
        if divisor>math.sqrt(x):
            break
        if x%divisor==0:
            return False
    primes.append(x)
    return True
#Prime factorization
def factorize(x):
    primefactors=[]
    divisor=2
    while x > 1:
        if(is_prime(divisor)):
            if x % divisor==0:
                x=x/divisor
                primefactors.append(divisor)
            else:
                divisor+=1
        else:
            divisor+=1
    return primefactors
#Total number of factors
def factors(m):
    p=1
    s=1
    params=factorize(m)
    params.append(0)
    l=len(params)
    l-=1
    for i in range(l):
        if params[i]==params[i+1]:
            p+=1
        else:
            p+=1
            s*=p
            p=1
    print("Number of factors:", s)

#Factors
print("Enter a Number:")
number = int(input())
factors(number)