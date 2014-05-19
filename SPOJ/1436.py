parent = [i for i in range(10010)]
hasCycle = False

def find(element):
	if parent[element] == element:
		return element
	else:
		parent[element] = find(parent[element])
		return parent[element]
		
def union(u, v):
	global hasCycle
	if find(u) == find(v):
		hasCycle = True
	else:
		parent[find(v)] = find(u)

def main():
	n, m = map(int, raw_input().split())
	edge = []
	if m != n - 1:
		print 'NO'
	else:
		for i in range(m):
			u, v = map(int, raw_input().split())
			edge.append([u, v])
		for item in edge:
			union(item[0], item[1])
			if hasCycle == True:
				print 'NO'
				exit()
		print 'YES'
			
if __name__ == '__main__':
	main()

