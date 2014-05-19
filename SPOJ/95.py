import sys

while True:
    n = int(sys.stdin.readline().split()[0])
    if n == 0:
        break
    order = sys.stdin.readline().split()
    order = [int(i) for i in order]
    need = 1
    flag = False
    stack = [99999]
    for i in order:
        if i != need:
            if stack[-1] != need:
                if stack[-1] < i:
                    print 'no'
                    flag = True
                    break
                else:
                    stack.append(i)
        else:
            need = i + 1
    if not flag:
        print 'yes'
