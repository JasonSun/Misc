import sys
s = sys.stdin.readline().split()
n = int(s[0])
w = int(s[1])
h = int(s[2])
#n, w, h = map(int, raw_input().split())
envelop = list()
dp = list()
chain = dict()
for i in range(n):
    s = sys.stdin.readline().split()
    wi = int(s[0])
    hi = int(s[1])
    #wi, hi = map(int, raw_input().split())
    if wi > w and hi > h:
        envelop.append((wi, hi, i + 1))
if len(envelop) == 0:
    print 0
else:
	envelop.sort(key = lambda tuple: (tuple[0], tuple[1])) # sort according to wi and hi
	dp = [1 for each in envelop]

	for i in range(len(envelop)):
	    for j in range(len(envelop[0:i])):
		if envelop[i][0] > envelop[j][0] and envelop[i][1] > envelop[j][1] and dp[j] + 1 > dp[i]:
		    dp[i] = dp[j] + 1
		    chain[envelop[i][2]] = envelop[j][2]

	result = list()
	print max(dp) # output the size of chain
	for i in range(len(dp)):
	    if dp[i] == max(dp):
		index = i
		break

	result.append(envelop[index][2])
	index = envelop[index][2]
	while True:
	    if index not in chain:
		break
	    else:
		result.append(chain[index])
		index = chain[index]
	result.reverse()
	for each in result:
	    print each,
