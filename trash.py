l = [1,2,3,4,1,1,2,2,3,3,4,5]
d = {}
for i in l:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1

    # print(l.count(i))

print(d)