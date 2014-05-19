nCase = input()
for i in range(nCase):
    first = raw_input().split()
    stamps = int(first[0])
    friends = int(first[1])
    second = raw_input().split()
    stampLst = [int(each) for each in second]
    stampLst.sort()
    stampLst.reverse()
    if sum(stampLst) < stamps:
        print 'Scenario #%d:' % (i + 1)
        print 'impossible'
        print
    else:
        for one in range(friends):
            if sum(stampLst[0:one + 1]) >= stamps:
                print 'Scenario #%d:' % (i + 1)
                print one + 1
                print
                break
