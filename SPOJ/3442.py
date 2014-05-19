import sys
digit = dict()
digit[2] = [2, 4, 8, 6]
digit[3] = [3, 9, 7, 1]
digit[4] = [4, 6]
digit[7] = [7, 9, 3, 1]
digit[8] = [8, 4, 2, 6]
digit[9] = [9, 1]
nCase = int(sys.stdin.readline().split()[0])
for i in range(nCase):
    inputLine = sys.stdin.readline().split()
    a = int(inputLine[0]) % 10
    b = int(inputLine[1])
    if a == 0 and b != 0:
        print 0
    elif a == 1 or b == 0:
        print 1
    elif a == 5:
        print 5
    elif a == 6:
        print 6
    else:
        print digit[a][(b - 1) % len(digit[a])]
