s = [int(i) for i in raw_input().split()]
lst = s[0:4]
a = s[4]
b = s[5]
lst.sort()
if lst[0] > a and lst[0] < b:
    print lst[0] - a
elif lst[0] == b:
    print b - a
elif lst[0] > b:
    print b - a + 1
else:
    print '0'
