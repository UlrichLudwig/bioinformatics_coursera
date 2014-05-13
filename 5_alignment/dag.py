from collections import defaultdict
from common import small_example, read_dataset
from itertools import count

def output_lcs(backt, src, snk, g):
    way = [snk]
    v = snk
    while v != src:
        v = backt[v]
        way.append(v)

    print('->'.join(map(str, way[::-1])))

def lcs(src, snk, g):
    dists = defaultdict(int)
    backt = defaultdict(int)

    def search_node(u, lev=0):
        #print(' ' * lev, u, end='-> ', sep='')
        for v, w in g[u]:
            if dists[u] + w > dists[v]:
                dists[v] = dists[u] + w
                backt[v] = u
                #print(backt[v])

            #print(v, end=':')
            #print(w, end='=')
            #print(dists[v], end=', ')
        #print()
        for v, w in g[u]:
            search_node(v, lev+1)

    search_node(src)
    return dists[snk], backt

    #s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]

    #for l in s:
    #    print(l)


inp = read_dataset()
#inp = read_dataset()
#print(inp)
source, sink = int(inp[0]), int(inp[1])
dd = defaultdict(list)
for fr, to in (l.split('->') for l in inp[2:]):
    dd[int(fr)].append(list(map(int, to.split(':'))))

l, backt = lcs(source, sink, dd)
print(l)
#for i, w in backt.items():
#    print(i, w)
output_lcs(backt, source, sink, dd)
#print(out)