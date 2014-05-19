import sys

flag = True
while True:
	s = sys.stdin.readline()
	if s == '  \n':
		break
	if flag:
		print 'Ready'
		flag = False
	s = s.split()[0]
	if s == 'pq' or s == 'qp' or s == 'bd' or s == 'db':
		print 'Mirrored pair'
	else:
		print 'Ordinary pair'
