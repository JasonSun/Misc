import sys
while True:
    lst = sys.stdin.readline().split()
    if len(lst) == 0:
        break
    n = int(lst[0])
    if n % 10 == 0 and n != 0:
        print '2'
    else:
        print '1'
        print n % 10
