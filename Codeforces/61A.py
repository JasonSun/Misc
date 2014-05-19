r = ''
# zip() built-in function
# Using * operator to unzip
for a, b in zip(raw_input(), raw_input()):
    if a != b:
        r += '1'
    else:
        r += '0'
print r

'''
s1 = raw_input()
s2 = raw_input()
s3 = ''
for i in xrange(len(s1)):
    if s1[i] != s2[i]:
        s3 = s3 + '1'
    else:
        s3 = s3 + '0'
print s3
'''
