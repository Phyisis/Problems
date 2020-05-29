import math
s = "".join(str(i) for i in range(int(1e6)))
print(math.prod([int(s[int(x)]) for x in [1e0, 1e2, 1e3, 1e4, 1e5, 1e6]]))