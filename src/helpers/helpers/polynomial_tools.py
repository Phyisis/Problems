import numpy as np

factors = {
        0:[0],
        1:[1],
        2:[1,2],
        3:[1,3],
        4:[1,2,4],
        5:[1,5],
        6:[1,2,3,6],
        7:[1,7],
        8:[1,2,4,8],
        9:[1,3,9],
    }

def derivative(u):
    degree = len(u)-1
    return [u[i]*(degree-i) for i in range(degree)]

def quo_rem(u,v):
    m = len(u) - 1
    n = len(v) - 1
    scale = 1./v[0]
    q = [0 for i in range(max(m - n + 1, 1))]
    r = u.copy()
    for k in range(0, m-n+1):
        d = scale*r[k]
        q[k] = d
        for i in range(n+1):
            r[k+i] -= d*v[i]
    while r[0]==0 and len(r)>1:
        r.pop(0)
    return q, r

def isRoot(u,x):
    if quo_rem(u,[1,-x])[1] == [0]:
        return True
    return False

def eval(f,x):
    degree = len(f)
    return sum([f[i]*x**(degree-i) for i in range(degree)])

# Count sign changes in a list of coefficients
# Example: If myList = [3,-2,0,-1,0,0,1,2,3], then this function returns 2 sign changes (zeros are ignored).
def signChange(myList):
    numList = myList[::]  # make a copy of the list of coefficients (don't overwrite myList).

    # Get rid of initial zeros.
    while numList and numList[0]==0:  # pop off elements as long as the list isn't empty and starts with 0.
        numList.pop(0)

    s = 0  # no sign changes yet.
    if numList:  # if the list isn't empty...
        cs = 1 if numList[0]>0 else -1  # cs = 1 for a first positive entry and -1 for negative.
        numList.pop(0)  # Pop off the first element
        while numList:  # Loop while there's more in the list. 
            # tmp = 1, -1, or the current sign cs according to whether the list begins with a positive, negative, or zero.
            tmp = 1 if numList[0]>0 else -1 if numList[0]<0 else cs  
            if tmp != cs: # the sign switched
                cs = tmp  # change the current sign
                s = s+1   # increment the number of sign changes
            numList.pop(0)  # pop off the first element in the list

    return s
    
def findRoots(p,a,b):
    # The derivative, p'(x), is the second term in the Sturm sequence.
    pPrime = derivative(p)

    # p'(x)=0 means p(x) is constant. Then everything is a root and Sturm's method doesn't apply - so quit.
    if pPrime==0:
        return
    
    # r is a Sturm sequence. It begins with p(x) and p'(x). tmp = (first quotient, first remainder)
    tmp = quo_rem(p,pPrime) 
    r=[p,pPrime]

    i=1

    # While we have yet to reach a zero remainder continue divisions tacking on the new
    # negative remainder to our list r.
    while r[i] != [0]:
        tmp = quo_rem(r[i-1],r[i]) 
        r.append([-1*j for j in tmp[1]])
        i=i+1
    # Remove the final negative remainder - it's zero.
    r.pop(-1) 

    # Plug x=a into the Sturm sequence. Then use "signChange" to count the number of sign changes.
    # If x=a is a repeated root, the canonical sequence will yield all zeros, so in this case we
    # divide by the final term to get a modified sequence which always works.
    if eval(r[-1],a) == 0:
        rAta = [eval(quo_rem(g,r[-1])[0],a) for g in r]
    else:
        rAta = [eval(g,a) for g in r]
    scAta = signChange(rAta)

    # Plug x=b into the Sturm sequence. Then use "signChange" to count the number of sign changes.
    # If x=b is a repeated root, the canonical sequence will yield all zeros, so in this case we
    # divide by the final term to get a modified sequence which always works.
    if eval(r[-1],b) == 0:
        rAtb = [eval(quo_rem(g,r[-1])[0],b) for g in r]
    else:
        rAtb = [eval(g,b) for g in r]
    scAtb = signChange(rAtb)

    # Sturm tells us the that the difference in sign changes at x=a and at x=b give us the number of roots in (a,b).
    realRoots = scAta - scAtb
    return realRoots

def sylvester(u, v):
    rows = []
    m = len(u)-1
    n = len(v)-1
    size = m + n
    for i in range(size):
        row = []
        if i in range(0, n):
            row = u.copy()
            row.extend((n-1-i)*[0])
            row[:0] = [0]*i
            rows.append(row)
        if i in range(n, size):
            row = v.copy()
            row.extend((size-1-i)*[0])
            row[:0] = [0]*(size-len(row))
            rows.append(row)
    return rows

def getOptimalSylvester(u):
    sp = [
        [0],
        [1,1],
        [1,3,2],
        [1,6,11,6],
        [1,10,35,50,24],
        [1,15,85,225,274,120],
        [1,21,175,735,1624,1764,720],
        [1,28,322,1960,6769,13132,13068,5040],
        [1,36,546,4536,22449,67284,118124,109584,40320],
        [1,45,870,9450,63273,269325,723680,1172700,1026576,362880]
    ]
    return sylvester(u,sp[u[-1]])

def hasIntegerRoot(u):
    if np.linalg.det(np.array(getOptimalSylvester(u))) == 0:
        return True
    return False