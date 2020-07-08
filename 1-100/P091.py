from helpers import analytics
analytics.monitor()

def dot(ax,ay,bx,by):
    return ax*bx+ay*by

def main():
    limit = 51
    total = 0
    for ax in range(limit):
        for ay in range(limit):
            if ax==0 and ay==0:
                continue
            for bx in range(limit):
                for by in range(limit):
                    if bx == 0 and by == 0:
                        continue
                    if ax == bx and ay == by:
                        continue
                    if (ax == 0 and by == 0):
                        total += 1
                    else:
                        if dot(ax,ay,bx-ax,by-ay)==0:
                            total += 1
    return total

print(main(), analytics.lap(), analytics.maxMem())
