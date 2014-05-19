d, sumTime = map(int, raw_input().split())
time = list()
schedule = list()
sumMaxtime = sumMintime = 0
for i in range(d):
    minTime, maxTime = map(int, raw_input().split())
    time.append((minTime, maxTime))
    sumMaxtime += maxTime
    sumMintime += minTime

if sumMaxtime < sumTime or sumMintime > sumTime:
    print 'NO'
else:
    for i in range(d):
        schedule.append(time[i][0])
    left = sumTime - sumMintime
    for i in range(d):
        schedule[i] += min(time[i][1] - time[i][0], left)
        left -= min(time[i][1] - time[i][0], left)
        if left == 0:
            break
    print 'YES'
    for i in range(d):
        print schedule[i],
