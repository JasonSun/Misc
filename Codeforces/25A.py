n = input()
l = map(int, raw_input().split())
for i, ele in enumerate(l):
    if ele % 2 == 0:
        l[i] = 0
    else:
        l[i] = 1
if l.count(0) == 1:
    print l.index(0) + 1
else:
    print l.index(1) + 1
