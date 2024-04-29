from helpers import analytics
analytics.monitor()


n_min = 900
n_max = 999

def Palindrome(n):
        temp = str(n)
        for i in range(0,len(temp)-1):
                if temp[i] != temp[len(temp)-1-i]:
                        return False
        return True

def main():
    for i in range(n_max,n_min,-1):
            for j in range(n_max,n_min,-1):
                    if Palindrome(i*j):
                            print(i*j)


print(main(), analytics.lap(), analytics.maxMem())
"""
906609
886688
888888
861168
888888
861168
886688
824428
906609
819918
824428
819918
None 
time: 0.009695014000000002 
max memory: 8.8MB
"""
