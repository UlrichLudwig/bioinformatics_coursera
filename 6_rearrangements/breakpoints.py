from itertools import count
from common import small_example, read_dataset, big_example, write_result


def breakpoints(permut):
    for v1, v2 in zip([0] + permut, permut + [len(permut) + 1]):
        if v2 - v1 != 1:
            #print(v1, v2)
            yield 1



if __name__ == '__main__':
    inp, out = small_example()
    #inp, out = big_example()
    inp = read_dataset()
    premut = list(map(int, inp[1:-1].split()))
    res = sum(breakpoints(premut))

    print(res)