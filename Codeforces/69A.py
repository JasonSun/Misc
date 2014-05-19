n = input()
x, y, z = 0, 0, 0
for i in range(n):
    lst = map(int, raw_input().split())
    x += lst[0]
    y += lst[1]
    z += lst[2]
if x == 0 and y == 0 and z == 0:
    print 'YES'
else:
    print 'NO'
