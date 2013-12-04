from common import small_example, big_example, read_dataset, write_result
from eulerian_cycle import eulerian_path
from debruijn import debruijn_graph
from collections import Counter
from itertools import chain


def assemble_contigs(adjlist):
    if not adjlist: return []
    graph = {u: vs for u, vs in adjlist.items()}

    vertives = set(chain(graph.keys(), chain.from_iterable(graph.values())))
    ins = dict.fromkeys(vertives, 0)
    outs = dict.fromkeys(vertives, 0)
    for u, vs in graph.items():
        outs[u] += len(vs)
    for v in chain.from_iterable(graph.values()):
        ins[v] += 1
    print('ins', ins)
    print('outs', outs)

    contig_starts = [v for v, out in outs.items() if not (out in (0, 1) and ins[v] == 1)]
    print('contig_starts', contig_starts)

    contigs = []
    for start in contig_starts:
        while graph[start]:  # multiple edges
            path = [start]
            u = graph[start].pop()
            while ins[u] == outs[u] == 1:
                path.append(u)
                u = graph[u].pop()
            contigs.append(''.join(v[0] for v in path) + u)

    return contigs


if __name__ == '__main__':
    #dataset, test_contigs = big_example()
    dataset = read_dataset()

    dataset = [l.lower() for l in dataset]
    adjlist = debruijn_graph(dataset)
    contigs = sorted(assemble_contigs(adjlist))
    #print(len(contigs))
    #test_contigs = sorted(test_contigs)
    #print(len(test_contigs))
    write_result('\n'.join(sorted(contigs)))