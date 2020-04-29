if __name__ == "__main__":
    n = int(input())
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    print("Factorial is = {}".format(fact))