while True:
    col = input()
    if col == 0:
        break
    else:
        msg = raw_input()
        row = len(msg) / col
        cnt = 0
        store = list()
        tmpList = list()
        for i in range(row):
            if i % 2 == 0:
                for j in range(col):
                    tmpList.append(msg[cnt])
                    cnt += 1
                store.append(tmpList)
                tmpList = []
            else:
                for j in range(col):
                    tmpList.append(msg[cnt])
                    cnt += 1
                tmpList.reverse()
                store.append(tmpList)
                tmpList = []
        for j in range(col):
            print store[0:row][j]
