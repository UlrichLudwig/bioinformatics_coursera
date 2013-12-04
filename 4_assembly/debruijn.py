from collections import defaultdict
from composition import composition
from itertools import count


def debruijn_graph_from_genome(k, genome):
    return debruijn_graph(composition(k, genome))


def debruijn_graph(kmers):
    adjlist = defaultdict(list)
    edges = kmers
    for e in edges:
        adjlist[e[:-1]].append(e[1:])
    return adjlist


def adjlist_tostr(adj_list):
    return '\n'.join((v + ' -> ' + ','.join(u) for v, u in sorted(adj_list.items()))) + '\n'


if __name__ == '__main__':
    with open('dataset.txt') as f:
        text = f.read()

    #genome = 'TAATGCCATGGGATGTT'
    #genome2 = 'TAATGGGATGCCATGTT'
    #adj_list_2 = debruijn_graph(2, genome)
    #adj_list_3 = debruijn_graph(3, genome)
    #adj_list_32 = debruijn_graph(3, genome2)
    #adj_list_4 = debruijn_graph(4, genome)
    #print(adjlist_tostr(adj_list_2))
    #print(adjlist_tostr(adj_list_3))
    #print(adjlist_tostr(adj_list_32))
    #print(adjlist_tostr(adj_list_4))

    adjlist = debruijn_graph(text.split())
    output = adjlist_tostr(adjlist)

    print(output)
    with open('result.txt', 'w') as r:
        print(output, file=r)