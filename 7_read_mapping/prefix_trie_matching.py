from collections import namedtuple, defaultdict
from itertools import count, chain
from operator import neg
from Bio.Seq import Seq
from common import small_example, read_dataset, big_example, write_result
from trie import trie


def prefix_trie_matching(text, trie):
    text = iter(text)
    nuc = next(text, None)
    node = trie
    path = ''
    while True:
        next_node = next((n for n in node.edges if nuc == n.nuc), None)
        if next_node and nuc:
            path += nuc
            nuc = next(text, None)
            node = next_node
        elif not node.edges:
            return path
        else:
            return ''


def trie_matching(text, trie):
    occurences = defaultdict(list)
    for i in range(len(text)):
        postfix = text[i:]
        path = prefix_trie_matching(postfix, trie)
        if path:
            occurences[path].append(i)

    return occurences


if __name__ == '__main__':
    inp, out = small_example()
    #inp, out = big_example()
    inp = read_dataset()

    root, edges = trie(map(Seq, inp[1:]))
    occurences = trie_matching(Seq(inp[0]), root)

    positions = ''
    for p in inp[1:]:
        if p in occurences:
            positions += ' '.join(map(str, occurences[p])) + '\n'

    #positions = prefix_trie_matching(Seq(inp[0]), root)
    write_result(positions)