x = int(input())
count = []
temp = 0
while x % 2 == 0: temp += 1; x /= 2;
if temp: count.append(temp)

i = 3
while(i * i <= x):
    temp = 0
    while x % i == 0: temp += 1; x /= i
    if temp: count.append(temp)
    i += 2

if x > 2:
    count.append(1)

factors = 1
for i in count:
    factors *= (i+1)

print(factors)
