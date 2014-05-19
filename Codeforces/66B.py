n = input()
h = map(int, raw_input().split())
h = [999999] + h + [999999]
mx = 1

for i in xrange(1, n + 1):
    r = 1
    j = i
    while h[j - 1] <= h[j]:
        j -= 1
    r += i - j
    j = i
    while h[j + 1] <= h[j]:
        j += 1
    r += j - i
    mx = max(mx, r)
print mx
'''
n = input()
h = map(int, raw_input().split())
mx = list()

def traverseLeft(index, height, h):
    if index == 0:
        return 1
    else:
        if height >= h[index - 1]:
            return 1 + traverseLeft(index - 1, h[index - 1], h)
        else:
            return 1
        

def traverseRight(index, height, h):
    if index == len(h) - 1:
        return 1
    else:
        if height >= h[index + 1]:
            return 1 + traverseRight(index + 1, h[index + 1], h)
        else:
            return 1

if __name__ == '__main__':
    for i, item in enumerate(h):
        l = traverseLeft(i, item, h)
        r = traverseRight(i, item, h)
        mx.append(l + r - 1)

    print max(mx)
'''
