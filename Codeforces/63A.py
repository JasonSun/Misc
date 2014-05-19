n = input()
name = list()
role = list()
rat = list()
womanChild = list()
man = list()
captain = list()

for i in xrange(n):
    s = raw_input().split()
    name.append(s[0])
    role.append(s[1])

for i, item in enumerate(role):
    if item == 'rat':
        rat.append(name[i])
    if item == 'child' or item == 'woman':
        womanChild.append(name[i])
    if item == 'man':
        man.append(name[i])
    if item == 'captain':
        captain.append(name[i])

for item in rat:
    print item
for item in womanChild:
    print item
for item in man:
    print item
for item in captain:
    print item
