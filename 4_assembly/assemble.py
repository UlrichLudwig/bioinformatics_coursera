from common import small_example, big_example, read_dataset, write_result
from eulerian_cycle import eulerian_path


if __name__ == '__main__':
    dataset, _ = small_example()
    dataset = read_dataset()

    adjlist = {words[0]: set(words[1].split(','))
               for words in (l.split(' -> ') for l in dataset)}
    print(adjlist)
    path = eulerian_path(adjlist)

    output = ''.join(kmer[0] for kmer in path) + path[-1][1:]
    write_result(output)