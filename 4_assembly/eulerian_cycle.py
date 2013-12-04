from collections import defaultdict
import re
import itertools


def eulerian_cycle(adjlist, *args, **kwargs):
    if not adjlist: return []
    graph = {u: vs for u, vs in adjlist.items()}

    u = next(iter(graph.keys()))
    cycle = [u]
    while True:
        while u in graph and graph[u]:
            u = graph[u].pop()
            cycle.append(u)
        u = next((u for u in cycle if u in graph and graph[u]), None)
        if u is None:
            break
        i = cycle.index(u) + 1 % len(cycle)
        cycle = [u] + cycle[i:] + cycle[1:i]
    return cycle


def eulerian_path(adjlist, cycle_routine=eulerian_cycle, *args):
    if not adjlist: return []
    graph = {u: vs for u, vs in adjlist.items()}

    #print('edges num:', len(list(itertools.chain.from_iterable(graph.values()))))
    ins = defaultdict(int)
    outs = defaultdict(int)
    for u, vs in graph.items():
        for v in vs:
            outs[u] += 1
            outs[v] += 0
            ins[v] += 1
            ins[u] += 0

    odds = [u for u in ins.keys() if ins[u] != outs[u]]
    if len(odds) == 2:
        u, v = odds
        if outs[u] > ins[u]:
            u, v = v, u
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
    #print(u, v)
    #print('edges num:', len(list(itertools.chain.from_iterable(graph.values()))))

    cycle = cycle_routine(graph, *args, added=(u, v))
    #print('Cycle', len(cycle), ':', '->'.join(map(str, cycle)))

    if len(odds) == 0:
        return cycle

    for i in range(len(cycle) - 1):
        if cycle[i] == u:
            #print('Oppa!', cycle[i - 1:i + 2])
            if cycle[i + 1] == v:
                return cycle[i + 1:] + cycle[1:i + 1]
    raise Exception('No added edge in cycle')


def check_eulerian(adjlist, cycle):
    graph = {u: vs for u, vs in adjlist.items()}

    print()
    cycle = iter(cycle)
    u = next(cycle, None)
    while u is not None:
        v = next(cycle, None)
        if v is None:
            break

        if v not in graph[u]:
            print('no edge for (', u, ',', v, ')')
            break

        graph[u].remove(v)
        u = v

    print('left:')
    print(list(filter(None, graph.values())))
    print({u: vs for u, vs in graph.items() if vs})
    print()


def read_example():
    with open('example.txt') as t:
        input = []
        output = []
        reading_input = True
        for line in t.readlines():
            line = line.strip()
            if line == 'Input':
                continue
            if line == 'Output':
                reading_input = False
                continue
            if reading_input:
                input.append(line)
            else:
                output.append(line)
        return input, output


if __name__ == '__main__':
    example_dataset, example_output = read_example()
    dataset = open('dataset.txt').readlines()

    adjlist = {int(words[0]): set(map(int, words[2].split(',')))
               for words in (l.split() for l in dataset)}
    #cycle = eulerian_cycle(adjlist)
    path = eulerian_path(adjlist)

    output = '->'.join(map(str, path))
    print('\nOutput:', len(path), ':', output)
    open('result.txt', 'w').write(output)

    check_eulerian(adjlist, path)

    print('\nExample:', len(example_output[0].split('->')), ':', example_output[0])
    open('test_result.txt', 'w').write(example_output[0])
