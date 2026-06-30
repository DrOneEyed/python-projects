a = open(r'scores.txt','r')
b = open(r'result.txt','w+')
l = a.readlines()
s = list(map(int,l[0].split(',')))
n = l[1].split(',')
d = dict(zip(n,s))
s_d = {}
s_v = sorted(d.values())
for i in s_v:
    for j in d.keys():
        if d[j] == i:
            s_d[j] = d[j]
print(s_d)
ll = list(s_d.items())
b.write('Lowest score: {}'.format(ll[0]))
b.write('Median score: {}'.format(ll[len(ll)//2]))
b.write('Highest score: {}'.format(ll[-1]))
a.close()
b.close()
