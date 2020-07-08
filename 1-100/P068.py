from helpers import analytics
analytics.monitor()
from itertools import permutations

high = [10,9,8,7]
low = [1,2,3,4,5]
# outside: 0,1,2,3,4
# inside: 5,6,7,8,9
# arms: 0,5,6 - 1,6,7 - 2,7,8 - 3,8,9 - 4,9,5

def valid(s):
    m_sum = s[0] + s[5] + s[6]
    if m_sum == s[1] + s[6] + s[7]:
        if m_sum == s[2] + s[7] + s[8]:
            if m_sum == s[3] + s[8] + s[9]:
                if m_sum == s[4] + s[9] + s[5]:
                    return True
    return False

def output(s):
    r = [s[0],s[5],s[6],s[1],s[6],s[7],s[2],s[7],s[8],s[3],s[8],s[9],s[4],s[9],s[5]]
    return int(''.join(map(str,r)))

def main():
    solution = []
    for o in permutations(high):
        for i in permutations(low):
            s = [6] + list(o) + list(i)
            if valid(s):
                solution.append(output(s))
    return max(solution)

print(main(), analytics.lap(), analytics.maxMem())