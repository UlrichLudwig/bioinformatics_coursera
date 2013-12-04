from collections import OrderedDict
import re


def overlap_graph(kmers):
    adj_list = []  # dict(zip(kmers, ([] for _ in count())))
    for v in sorted(kmers):
        for u in kmers:
            if v[1:] == u[:-1]:
                if u == v:
                    print(u)
                adj_list.append((v, u))
                break
    return adj_list


def example():
    with open('example.txt') as t:
        input, output = re.match(r'Input\n(\S+)\nOutput\n(\S+)\n', t.read()).groups()
        return input


if __name__ == '__main__':
    example_dataset, example_output = example()
    print('example len', len(list(example_output.split('\n'))))

    with open('dataset.txt') as f:
        dataset = f.read()

    adj_list = overlap_graph(example_dataset.split())

    print('res len', len(adj_list))

    result = '\n'.join((v + ' -> ' + u for v, u in adj_list))

    with open('result.txt', 'w') as r:
        print(result, file=r)
