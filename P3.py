import math

n = 600851475143

min = 3
max = math.floor(n**(.5))

while (n > 1):
        for i in range(min,max,2):
                if n % i == 0:
                        print(i)
                        n = n/i



