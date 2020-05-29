def factorize(n):
    pf = []
    for i in range(3,int(n**(.5)),2):
        while n % i == 0:
            pf.append(i)
            n //= i
    return pf

num = 600851475143
print(factorize(num))