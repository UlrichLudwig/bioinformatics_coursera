from itertools import product
from common import small_example, big_example, read_dataset, write_result
from eulerian_cycle import eulerian_path, eulerian_cycle
from debruijn import debruijn_graph


if __name__ == '__main__':
    kmers = (''.join(kmer) for kmer in product('01', repeat=17))
    adjlist = debruijn_graph(kmers)
    cycle = eulerian_cycle(adjlist)

    output = ''.join(kmer[0] for kmer in cycle[:-1])
    write_result(output)