s = raw_input()
u = l = 0
'''
Concise style
u = sum(c.isupper() for c in s)
'''
for c in s:
    if c.isupper():
        u += 1
    else:
        l += 1
if l >= u:
    print s.lower()
else:
    print s.upper()
