from collections import namedtuple
from itertools import count, chain
from operator import neg
from Bio.Seq import Seq
from common import small_example, read_dataset, big_example, write_result
from suffix_tree import SuffixTree, GeneralisedSuffixTree


class Node:
    def __init__(self, seq):
        self.seq = seq
        self.nuc = seq if len(seq) == 1 else None
        self.nodes = dict()

    def is_leaf(self):
        return False

    def __repr__(self):
        return self.seq + ': ' + str(len(self.nodes))


class Leaf(Node):
    def __init__(self, seq, pos):
        Node.__init__(self, seq)
        self.pos = pos

    def is_leaf(self):
        return True

    def __repr__(self):
        return super().__repr__() + ', pos: ' + str(self.pos)


class SuffixTrie:
    def __init__(self, text):
        self.text = text
        self.root = Node('')

        print(len(text))
        for i in range(len(text)):
            print(i)
            node = self.root
            for j in range(i, len(text) + 1):
                nuc = text[j] if j < len(text) else '$'
                next_node = node.nodes.get(nuc, None)
                if not next_node:
                    next_node = Node(nuc) if nuc != '$' else Leaf(nuc, i)
                    node.nodes[nuc] = next_node
                node = next_node

    def longest_repeat(self):
        longest_repeat = ''
        queue = [(self.root, self.root.seq)]
        while queue:
            node, way = queue.pop()
            if len(node.nodes) > 1:
                if len(way) > len(longest_repeat):
                    longest_repeat = way
                    print(longest_repeat)

            queue.extend(zip(
                node.nodes.values(),
                (way + seq for seq in node.nodes.keys())
            ))

        print('-' * len(longest_repeat))
        return longest_repeat


    def indexof(self, seq):
        node = self.root
        for i, nuc in enumerate(seq):
            node = node.nodes.get(nuc, None)
            if not node:
                return None

        indices = []
        queue = [node]
        while queue:
            node = queue.pop()
            if node.is_leaf():
                indices.append(node.pos)
            else:
                queue.extend(node.nodes.values())
        return indices


def longest_repeat(stree):
    max_repeat = ''
    for n in stree.innerNodes:
        #print(n.pathLabel)
        if len(n.pathLabel) > len(max_repeat):
            #print('max!')
            max_repeat = n.pathLabel
    print(max_repeat)


if __name__ == '__main__':
    inp, out = small_example()
    #inp, out = big_example()
    #inp = read_dataset()

    seqs = inp

    #stree = SuffixTree(seqs[1])

    #longest_shared = ''
    #for shared in stree.sharedSubstrings():
    #    for seq, start, stop in shared:
    #        s = seqs[seq][start:stop]
    #        #print(s)
    #        if len(s) > len(longest_shared):
    #            longest_shared = s
    #
    #print(longest_shared)


    #for l in stree.leaves:
    #    print(l.pathLabel)


    #shortest = seqs[0]
    #
    #for l in range(1, len(seqs[0])):
    #    for i in range(0, len(seqs[0]) - l + 1):
    #        s = seqs[0][i:i + l]
    #        #print(s)
    #        bad = False
    #        for lv in stree.leaves:
    #            if lv.pathLabel.startswith(s):
    #                bad = True
    #                continue
    #        if not bad:
    #            if len(s) < len(shortest):
    #                shortest = s
    #                print(s)
    #
    #print(shortest)


    stree = SuffixTree(seqs[0] + seqs[1])

    shortest = seqs[0]
    for l in stree.leaves:
        print(l.pathLabel)
        if len(l.pathLabel) < len(shortest):
            shortest = l.pathLabel

    print(shortest)


    #print(list((n.pathLabel for n in stree.innerNodes)))

    #res = ''
    #for l in stree.postOrderNodes:
    #    print(l.edgeLabel)
    #    res += l.edgeLabel + '\n'
    #
    #write_result(res)

    #print(sf.indexof('TATCGTT'))

    #print(sf.longest_repeat())