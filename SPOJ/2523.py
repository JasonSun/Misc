nCase = input()
for i in range(nCase):
    lst = raw_input().split()
    indicate = int(lst[0])
    string = list(lst[1])
    string.pop(indicate - 1)
    print i + 1, ''.join(string)
