# find x, where x**2 = 1_2_3_4_5_6_7_8_9_0

#seems like must end in 900, and therefore x ends in 30 or 70
#min = 1.01e9, max = 1.39e9
from helpers import analytics
analytics.monitor()

def main():
    for x in range(1010000070,1400000070,100):
        if str(x**2)[0::2]=="1234567890":
            return x

print(main(), analytics.lap(), analytics.maxMem())