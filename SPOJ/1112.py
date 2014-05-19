result = list()
result.append([0, 0, -1, 1])
tip = 1
for i in range(5010):
    result.append([tip + 1, tip + 3, tip + 2, tip + 4])
    tip += 4
N = input()
for i in range(N):
    s = raw_input()
    x = int(s.split()[0])
    y = int(s.split()[1])
    if y != x - 2 and y != x:
        print 'No Number'
    else:
        if x % 2 == 0:
            if y == x - 2:
                print result[x / 2][0]
            else:
                print result[x / 2][1]
        else:
            if y == x - 2:
                print result[(x - 1) / 2][2]
            else:
                print result[(x - 1) / 2][3]
