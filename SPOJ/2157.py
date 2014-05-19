import sys

nCase = int(sys.stdin.readline().split()[0])
for i in range(nCase):
    sys.stdin.readline()
    lst = sys.stdin.readline().split()
    lst.pop(1)
    lst.pop(2)
    if 'machula' in lst[0]:
        b = int(lst[1])
        total = int(lst[2])
        a = total - b
    elif 'machula' in lst[1]:
        a = int(lst[0])
        total = int(lst[2])
        b = total - a
    else:
        a = int(lst[0])
        b = int(lst[1])
        total = a + b
    sys.stdout.write('%d + %d = %d\n' % (a, b, total))
