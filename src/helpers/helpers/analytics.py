import time, psutil

start = time.perf_counter()
step = start
mem = None

def lap():
    global step
    now = time.perf_counter()
    diff = now - step
    step = now
    return "\n" + "time: " + str(diff)

def monitor():
    global mem
    mem = psutil.Process()

def maxMem():
    return "\n" + "max memory: " + sizeof_fmt(mem.memory_info().rss)

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G']:
        if abs(num) < 1024:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024
    return "%.1f%s%s" % (num, 'T', suffix)
