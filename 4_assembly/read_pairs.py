from collections import defaultdict, Counter
from itertools import chain
from composition import composition
from eulerian_cycle import eulerian_path
from debruijn import debruijn_graph
from common import small_example, big_example, read_dataset, write_result


def paired_dubruijn(pairs):
    adjlist = defaultdict(list)
    for l, r in pairs:
        adjlist[(l[:-1], r[:-1])].append((l[1:], r[1:]))
    return adjlist


#def paired_path(adjlist, d):
#    def choose(l_node, exts):
#        for ext in exts:
#            if ext[0] == l_node[1]:
#                exts.remove(ext)
#                return ext
#        return None
#
#    if not adjlist: return []
#    graph = {u: vs for u, vs in adjlist.items()}
#
#    u = next(u for u in graph.keys() if u not in chain(*adjlist.values()))
#    path = [u]
#    while u in graph and graph[u]:
#        if len(path) < d:
#            u = graph[u].pop()
#        else:
#            u = choose(path[-d], graph[u])
#        if u:
#            path.append(u)
#    return path


def paired_path(adjlist, d):
    if not adjlist: return []
    graph = {u: vs for u, vs in adjlist.items()}

    def choose(l_node, exts):
        for ext in exts:
            if ext[0][-1] == l_node[1][0]:
                exts.remove(ext)
                return ext
        return None

    flow = Counter()
    for u, vs in graph.items():
        flow[u] -= len(vs)
    for v in chain.from_iterable(graph.values()):
        flow[v] += 1

    path_len = len(list((chain.from_iterable(graph.values()))))
    print(path_len)

    u = next((v for v, c in flow.items() if c == -1), None)
    cycle = [u]
    while True:
        while u in graph and graph[u]:
            if len(cycle) <= d + 1:
                u = graph[u].pop()
            else:
                u = choose(cycle[-(d + 2)], graph[u])
            if u:
                cycle.append(u)
        u = next((u for u in cycle if u in graph and graph[u]), None)
        if u is None:
            break
        i = cycle.index(u) + 1 % len(cycle)
        cycle = [u] + cycle[i:] + cycle[1:i]
    return cycle


#def paired_path(adjlist, d):
#    if not adjlist: return []
#    graph = {u: vs for u, vs in adjlist.items()}
#    return eulerian_path(adjlist, paired_cycle, d)


if __name__ == '__main__':
    #k, d = 3, 2
    #genome = 'TAATGCCATGGGATGTT'
    #long_comp = composition(k + d + k, genome)
    #pairs = sorted((long[:k], long[-k:]) for long in long_comp)
    #print(', '.join('(' + '|'.join(pair) + ')' for pair in pairs))

    #data = '(AG|AG) → (GC|GC) → (CA|CT) → (AG|TG) → (GC|GC) → (CT|CT) → (TG|TG) → (GC|GC) → (CT|CA)'
    #pairs = (tuple(pair[1:-1].split('|')) for pair in data.split(' → '))
    #k, d = 2, 1
    data = read_dataset()
    d = int(data[0])
    pairs = [line.split('|') for line in data[1:]]
    k = len(pairs[0][0])
    adjlist = paired_dubruijn(pairs)

    path = paired_path(adjlist, d)
    print(path)

    genome = ['-' for _ in range(len(pairs) + k + d + k - 1)]
    print(''.join(genome))
    l, r = path[0]
    for i, (l, r) in enumerate(path):
        for j, c in enumerate(l + '-' * (d + 1) + r):
            if c != '-':
                genome[i + j] = c
    print(''.join(genome))
