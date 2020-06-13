from helpers import analytics
analytics.monitor()

def main(n):
    pf = []
    for i in range(3,int(n**(.5)),2):
        while n % i == 0:
            pf.append(i)
            n //= i
    return pf

num = 600851475143
print(main(num), analytics.lap(), analytics.maxMem())