from helpers import analytics
analytics.monitor()

def count(S, n, N, lookup = {}):
    if (N == 0):
        return 1
    if (N < 0 or n < 0):
        return 0
    key = str(n) + "|" + str(N)
    if (key not in lookup):
        include = count(S, n, N - S[n], lookup)
        exclude = count(S, n - 1, N, lookup)
        lookup[key] = include + exclude        
    return lookup[key]

def main():
    currency = [1,2,5,10,20,50,100,200]
    goal = 200
    return count(currency,len(currency)-1,goal)

print(main(), analytics.lap(), analytics.maxMem())

