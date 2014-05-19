nCase = input()
for i in range(nCase):
    rev = raw_input().split()
    mInt = eval(rev[0][-1::-1].lstrip('0'))
    nInt = eval(rev[1][-1::-1].lstrip('0'))
    result = str(mInt + nInt)[-1::-1].lstrip('0')
    print eval(result)
