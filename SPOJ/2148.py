import sys

nCase = int(sys.stdin.readline().split()[0])
for i in range(nCase):
    sys.stdin.readline()
    candies = []
    nChildren = int(sys.stdin.readline().split()[0])
    for child in range(nChildren):
        candies.append(int(sys.stdin.readline().split()[0]))
    if sum(candies) % nChildren == 0:
        print 'YES'
    else:
        print 'NO'
