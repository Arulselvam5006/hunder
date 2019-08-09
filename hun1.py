s1 = int(input())
arul = [x for x in input().split()]
arul = []
for i in arul:
    if arul.count(i) > 1:
        arul.append(i)
if len(arul) == 0:
    print('unique')
else:
    print(' '.join(sorted(set(arul))))
