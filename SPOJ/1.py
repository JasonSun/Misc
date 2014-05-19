import sys

inputNum = sys.stdin.read().splitlines()
inputNum = [int(i) for i in inputNum]
for i in inputNum:
    if i == 42:
        break
    print i
