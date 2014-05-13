from collections import namedtuple
from itertools import count, chain
from operator import neg
from Bio.Seq import Seq
from common import small_example, read_dataset, big_example, write_result


def trie(patterns):
    all_edges = []
    Node = namedtuple('Node', 'i nuc edges')
    root = Node(1, '', [])

    nodes = 1
    for p in patterns:
        node = root
        for i, pnuc in enumerate(p):
            next_node = next((e for e in node.edges if pnuc == e.nuc), None)
            if not next_node:
                nodes += 1
                next_node = Node(nodes, pnuc, [])
                node.edges.append(next_node)
                all_edges.append((node.i, next_node.i, pnuc))
            node = next_node

    return root, all_edges

    #edges = [(1, i, p[0]) for i, p in zip(count(0), patterns)]
    #print(edges)
    #
    #prev_level_edges = {n: t for (f, t, n) in edges}
    #for i, prev_ns, next_ns in zip(count(),
    #                               [p[1:] for p in patterns],
    #                               [p[:1] for p in patterns]):
    #    new_level_edges = []
    #    for pn, nn in zip(prev_ns, next_ns):
    #        new_level_edges[pn] =
    #
    #
    #    for l in i_letters:
    #        if
    #
    #    prev_level_edges = level_edges


if __name__ == '__main__':
    inp, out = small_example()
    #inp, out = big_example()
    inp = read_dataset()

    root, edges = trie(map(Seq, inp))
    write_result('\n'.join('%d %d %s' % (f, t, n) for f, t, n in edges))