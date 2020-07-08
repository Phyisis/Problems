# lots of code from misreading the question
# implementation of Sturm's rule, polynomial division, derivative
import repackage; repackage.up()
from helpers import analytics,primes
analytics.monitor()
import random, math, itertools

def printPoly(p):
    x = [p[j]+"x^"+str(len(p)-j-1)+" + " for j in range(len(p))]
    print((''.join(x)).replace("^1 "," ")[:-6])

def eval(f,x):
    val = f[0]
    for i in range(1,len(f)):
        val = val*x+f[i]
    return val

def checkForRoots(i):
    p = [int(d) for d in str(i)]
    for x in range(-p[-1],1):
        if eval(p,x)==0:
            #print(i)
            return True
    return False

def fib(x):
    root5 = 5**0.5
    return int(((1+root5)**x-(1-root5)**x)/(root5*2**x))

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def digitSet(digits,limit):
    r = len(str(limit))-2
    return [int(''.join(i)) for i in itertools.product(digits,repeat=r) if i[-1] != "0"]

def digitSetAlt(digits,nonConsec,limit):
    r = len(str(limit))-2
    consec = digits - nonConsec
    s = [[d] for d in digits if d != "0"]
    while len(s[0]) < r:
        for i in range(len(s)):
            if s[i][-1] in consec:
                for d in nonConsec:
                    n = s[i].copy()
                    n.append(d)
                    s.append(n)
            for d in consec - {"0"}:
                n = s[i].copy()
                n.append(d)
                s.append(n)
            s[i].append("0")
    return [int(''.join(i)) for i in s]

#print(len(digitSet(["0","1","2"],int(1e16))))
#print(digitSetAlt({"0","1"},{"1"},int(1e7)))

def search1(limit):
    #this works for the example but way too slow to reach 1e16
    total = limit//10
    bd = {10:total,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0}
    for i in range(1,limit):
        if i%10==0: continue
        p = [int(d) for d in str(i)]
        for j in range(11,p[-1]+11):
            if i % j == 0:
                if eval(p,10-j)==0:
                    bd[j]+=1
                    total += 1
                    #break
    print(bd)
    return total

def search2(limit,x):
    #bitset = digitSet(["0","1"],limit)
    #bitset = digitSetAlt({"0","1"},{"1"},limit)
    #print(len(bitset))
    #print(bitset)
    total = 0
    for i in range(1,limit):
        if i%10==0: continue #include zeros?
        if i % x == 0:
            p = [int(d) for d in str(i)]
            if eval(p,10-x)==0:
                #print(i,i//x)
                total += 1
    return total

def bitSearch(limit):
    total = limit//10
    counted = set([])
    #bd = {10:total,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0}
    """
    i = 11
    while i < limit:
        if i % 10 == 0: i += 11; continue
        p = [int(d) for d in str(11*i)]
        if eval(p,-1)==0:
            counted.add(i)
            #bd[11]+=1
            total += 1
        i += 11
    i = 12
    while i < limit:
        if i % 10 == 0: i += 12; continue
        p = [int(d) for d in str(12*i)]
        if eval(p,-2)==0 and i not in counted:
            counted.add(i)
            #bd[12]+=1
            total += 1
        i += 12
    for a in digitSet(["0","1","2","3"],limit):
        i=13*a
        if i % 10 == 0: continue
        p = [int(d) for d in str(i)]
        if eval(p,-3)==0 and i not in counted:
            counted.add(i)
            #bd[13]+=1
            total += 1
    for a in digitSetAlt({"0","1","2"},{"2"},limit):
        i=14*a
        if i % 10 == 0: continue
        p = [int(d) for d in str(i)]
        if eval(p,-4)==0 and i not in counted:
            counted.add(i)
            #bd[14]+=1
            total += 1
    """
    for a in digitSet(["0","1"],limit):
        for j in range(15,19):
            i = j*a
            if i % 10 == 0: continue
            p = [int(d) for d in str(i)]        
            if eval(p,10-j)==0 and i not in counted:
                counted.add(i)
                #bd[j]+=1
                total += 1
    for a in digitSetAlt({"0","1"},{"1"},limit):
        i=19*a
        if i % 10 == 0: continue
        p = [int(d) for d in str(i)]
        if eval(p,-9)==0 and i not in counted:
            counted.add(i)
            #bd[19]+=1
            total += 1
    #print(bd)
    return total

def bitSearch2(limit):
    total = limit//10
    q = set([])
    #bd = {10:total,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0}
    i = 11
    while i < limit:
        if i % 10 == 0: i += 11; continue
        p = [int(d) for d in str(11*i)]
        if eval(p,-1)==0:
            #bd[11]+=1
            total += 1
        i += 11
    i = 12
    while i < limit:
        if i % 10 == 0: i += 12; continue
        p = [int(d) for d in str(12*i)]
        if eval(p,-2)==0:
            #bd[12]+=1
            total += 1
        i += 12
    for a in digitSet(["0","1","2","3"],limit):
        i=13*a
        if i % 10 == 0: continue
        p = [int(d) for d in str(i)]
        if eval(p,-3)==0:
            #bd[13]+=1
            total += 1
    for a in digitSetAlt({"0","1","2"},{"2"},limit):
        i=14*a
        if i % 10 == 0: continue
        p = [int(d) for d in str(i)]
        if eval(p,-4)==0:
            #bd[14]+=1
            total += 1
    for a in digitSet(["0","1"],limit):
        for j in range(15,19):
            i = j*a
            if i % 10 == 0: continue
            p = [int(d) for d in str(i)]        
            if eval(p,10-j)==0:
                #bd[j]+=1
                total += 1
    for a in digitSetAlt({"0","1"},{"1"},limit):
        i=19*a
        if i % 10 == 0: continue
        p = [int(d) for d in str(i)]
        if eval(p,-9)==0:
            #bd[19]+=1
            total += 1
    #print(bd)
    return total

#number of polys with roots -8 to -5: 2^(len(str(limit))-2) (maybe including dupes of -4 to -1)
#number of polys with root -9: fib(len(str(limit))-2) (maybe including dupes -4 to -1)

#limit = int(1e16)+1
#print(len(str(limit))-2,search2(limit,14))
#print("search2 time:", lap())
#print(search1(limit))
#print("search1 time:", lap())
#print(bitSearch(limit))
#print("bitSearch time:", lap())

def main(D):
    x = {(0,0,0,0,0,0,0,0,0,0): 1} #(values at 0 to -9): count of P
    for _ in range(D):
        y = x
        x = {} 
        for a in y: 
            for d in range(10): #add a digit
                b = tuple((None if d else 0) if i == 0
                        else None if a[i] is None
                        else (d - a[i]) // i if (d - a[i]) % i == 0
                        else None for i in range(10)) #check root at i
                if b in x:
                    x[b] += y[a]
                else:
                    x[b] = y[a]
    return sum(x[a] for a in x.keys() if any(aa == 0 for aa in a))


print(main(16), analytics.lap(), analytics.maxMem())