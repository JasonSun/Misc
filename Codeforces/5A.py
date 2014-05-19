import sys

name = set()
total = 0
'''
str.split() function ---> generate a list of str
str.strip() function ---> operate directly on str itself
sys.stdin.readlines() ---> a list of lines
'''
s = [each.strip() for each in sys.stdin.readlines()]
for each in s:
    if each[0] == '+':
        name.add(each[1:])
    elif each[0] == '-':
        name .remove(each[1:])
    else:
        msg = each.split(':')[1]
        total += len(msg) * len(name)

print total
