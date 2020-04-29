n = int(input('Enter the Number'))
N_f = 2
f = 2
while f*f <= n:
    if(n%f == 0):
        if f*f != n:
            N_f += 2
        else:
            N_f += 1
    f+=1
print(N_f)