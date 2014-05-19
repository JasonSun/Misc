n = input()
person = dict() # store name:score item
sequence = list() # store play rounds sequence
for i in range(n):
    s = raw_input().split()
    name = s[0]
    person.setdefault(name, 0)
    score = int(s[1])
    person[name] += score
    sequence.append((name, person[name]))

maxScore = max(person.values()) # The max score in these persons

for name, score in sequence:
    if person[name] == maxScore and score >= maxScore:
        print name
        break
