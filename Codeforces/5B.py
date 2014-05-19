import sys
maxChars = 0
flag = True
s = [each.strip() for each in sys.stdin.readlines()]
for each in s:
    if len(each) > maxChars:
        maxChars = len(each)
print '*' * (maxChars + 2)
for each in s:
    if (maxChars - len(each)) % 2 == 0:
        space = (maxChars - len(each)) / 2
        print '*' + ' ' * space + each + ' ' * space + '*'
    else:
        space = (maxChars - len(each)) / 2
        if flag:
            print '*' + ' ' * space + each + ' ' * (space + 1) + '*'
            flag = False
        else:
            print '*' + ' ' * (space + 1) + each + ' ' * space + '*'
            flag = True
print '*' * (maxChars + 2)
