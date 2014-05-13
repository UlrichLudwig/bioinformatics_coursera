from itertools import count, chain
from operator import neg
from common import small_example, read_dataset, big_example, write_result


def dist(ps1, ps2):
    flatten = chain.from_iterable
    print(len(list(flatten(ps1))))
    es = list(flatten(zip(p, map(neg, p[1:] + [p[0]])) for p in ps1 + ps2))
    cycles = 0
    print(es)
    while es:
        cycles += 1
        i, o = es.pop()
        print(i, end=' ')
        while es:
            print('', o, end=' ')
            if o == i:
                break
            for v1, v2 in es:
                if o == v1:
                    o = v2
                    break
                if o == v2:
                    o = v1
                    break
            es.remove((v1, v2))
            if o not in (v1, v2):
                if o != i:
                    print('Warning: %d != %d, %s' % o, i, str(es))
                break
        print()
    return len(list(flatten(ps1))) - cycles


def read_perm(p):
    cycles = p[1:-1].split(')(')
    return [list(map(int, c.split())) for c in cycles]


if __name__ == '__main__':
    inp, out = small_example()
    inp, out = big_example()
    inp = read_dataset()

    print(dist(*map(read_perm, inp)))