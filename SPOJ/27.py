import sys
import psyco
psyco.full()

def main():
	ins = sys.stdin.read().split('\n') # input split into list
	nCase = int(ins[0])
	pos = 1
	for i in range(nCase):
		dic = dict()
		n = int(ins[pos]) # iCase total number
		for account in ins[pos + 1 : pos + n + 1]:
			if account in dic:
				dic[account] += 1
			else:
				dic[account] = 1
		lst = dic.keys()
		lst.sort()
		for account in lst:
			sys.stdout.write('%s %s\n' % (account, dic[account]))
		sys.stdout.write('\n')
		pos += n + 2

if __name__ == '__main__':
	main()
