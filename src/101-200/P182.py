from helpers import analytics, primes, integers
analytics.monitor()

p,q  = 1009,3643
n,phi = p*q,(p-1)*(q-1)
print(p,q,n,phi)

def encrypt(m,en,n):
    return pow(m,en,n)

def decrypt(c,de,n):
    return pow(c,de,n)

m = n//3
en = 1031 # gcd(e,phi) == 1
de = integers.mod_inv(e,phi) # e*d % phi == 1
c = encrypt(m,e,n)
print(m,c)
d = decrypt(c,e,n,phi)
print(m,c,d)


def main():
    return

print(main(), analytics.lap(), analytics.maxMem())