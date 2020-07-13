from helpers import analytics
analytics.monitor()

def main(limit):
    chainLength = [1]
    longest = 0
    gen = 0

    for i in range(2,limit+1):
        chain = 0
        while (i not in range(1,len(chainLength)+1)):
            if i % 2 == 0:
                i = int(i/2)
                chain += 1
            else:
                i = (3*i + 1)
                chain += 1
        chain += chainLength[i-1]
        chainLength.append(chain)

    for i in range(0,len(chainLength)):
        if (chainLength[i] > longest):
            longest = chainLength[i]
            gen = i+1

    return str(gen) + " generates a chain of length " + str(longest)


print(main(1000000), analytics.lap(), analytics.maxMem())




