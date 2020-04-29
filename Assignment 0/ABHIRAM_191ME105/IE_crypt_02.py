N, count = int(input("Enter a number : ")), 0
for i in range(1, int(N**0.5) + 1):
    if N%i == 0:
        if N == i*i:
            count += 1
        else:
            count += 2
print(count)
