from random import randint
from math import ceil, sqrt

s1 = input("Enter string 1:")
s2 = input("Enter string 2:")

len1, len2 = 0, 0

for ch in s1: len1 += 1
for ch in s2: len2 += 1

if len1 != len2:
    print("Not anagram")
    exit(0)

primes = []
primes.append(2)
primes_count, i = 1, 3
while(primes_count < 26):
    it_is_prime=1
    for j in range(2, ceil(sqrt(i))+1):
        if i % j == 0:
            it_is_prime=0
            break
    if it_is_prime:
        primes.append(i)
        primes_count += 1
    i += 2

prod1, prod2 = 1, 1

for ch in s1: prod1 *= primes[ord(ch)-97]
for ch in s2: prod2 *= primes[ord(ch)-97]

print("Anagram") if prod1 == prod2 else print("Not Anagram")
