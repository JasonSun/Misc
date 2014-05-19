import sys
while True:
    s = sys.stdin.readline().split()
    if not s:
        break
    n = int(s[0])
    m = int(s[1])
    a = int(s[2])
    if n % a == 0:
        r = n / a
    else:
        r = n / a + 1
    if m % a == 0:
        c = m / a
    else:
        c = m / a + 1
    print r * c
