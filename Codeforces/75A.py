a = input()
b = input()
c = a + b
a = str(a)
b = str(b)
c = str(c)
a = ''.join(a.split('0'))
b = ''.join(b.split('0'))
c = ''.join(c.split('0'))
if int(a) + int(b) == int(c):
    print 'YES'
else:
    print 'NO'

