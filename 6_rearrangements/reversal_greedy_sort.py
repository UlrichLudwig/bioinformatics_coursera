from itertools import count
from common import small_example, read_dataset, big_example, write_result

#GREEDYSORTING(P)
    #    approxReversalDistance ← 0
    #    for k = 1 to |P|
    #        if element k is not sorted
    #            apply the k-sorting reversal to P
    #            approxReversalDistance ← approxReversalDistance + 1
    #        if k-th element of P is −k
    #            apply the reversal flipping the k-th element of P
    #            approxReversalDistance ← approxReversalDistance + 1
    #    return approxReversalDistance

def greedy_sort(ini_permut):
    permuts = []
    permut = ini_permut
    pos = 0
    for pos in range(0, len(ini_permut)):
        if permut[pos] != pos + 1:
            for i, el in zip(count(pos), permut[pos:]):
                if abs(el) == pos + 1:
                    permut = permut[:pos] + [-a for a in permut[pos:i + 1][::-1]] + permut[i + 1:]
                    permuts.append(permut)
                    if -el < 0:
                        permut = permut[:pos] + [abs(permut[pos])] + permut[pos + 1:]
                        permuts.append(permut)
                    break

    return permuts


if __name__ == '__main__':
    inp, out = small_example()
    inp, out = big_example()
    inp = read_dataset()
    premut = list(map(int, inp[1:-1].split()))
    permuts = greedy_sort(premut)
    strs = ('(' + ' '.join(('+' if i > 0 else '') + str(i) for i in p) + ')' for p in permuts)

    #for s_mine, s_their in zip(strs, out):
    #    print(len(s_mine), len(s_their))
    #    for i, c_m, c_t in zip(count(), s_mine, s_their):
    #        if c_m != c_t:
    #            print(i)
    #            print(s_mine)
    #            print(s_their)
    #            print(c_m)
    #            print(c_t)
    #            input()

    str = '\n'.join(strs)
    write_result(str)
