import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "bin", "p079_keylog.txt")
keysFile = open(filename, "r")
keyLog = list(set([str(int(d)) for d in keysFile]))
keyLog.sort()
print(keyLog)

# 73162890, by hand