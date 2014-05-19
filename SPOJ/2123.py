import sys
while True:
    pN = int(sys.stdin.readline().split()[0])
    if pN == -1:
        break
    p = list()
    for i in range(pN):
        p.append(int(sys.stdin.readline().split()[0]))
    total = sum(p)
    if total % pN != 0:
        print -1
        continue
    p.sort()
    average = total / pN
    result = 0
    for i in p:
        if i < average:
            result += average - i
    print result
