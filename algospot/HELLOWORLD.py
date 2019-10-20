import sys


def rl():
    return sys.stdin.readline()


n = int(rl())
for i in range(n):
    print "Hello, %s!" % rl().strip()
