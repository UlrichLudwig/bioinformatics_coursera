from itertools import count, chain
from operator import neg
from Bio.Seq import Seq
from common import small_example, read_dataset, big_example, write_result


def syntenies(v, w, k):
    cw = w.complement()
    count = 0

    for i in range(0, len(v) - k + 1):
        block = v[i:i + k]

        j = w.find(block)
        ww = w
        while True:
            j = ww.find(block)
            if j != -1:
                j += len(w) - len(ww)
                print((i, j)) #, block, w[j:j + k])
                count += 1
                ww = w[j + 1:]
            else:
                break

        rcblock = block.reverse_complement()
        ww = w
        while True:
            j = ww.find(rcblock)
            if j != -1:
                j += len(w) - len(ww)
                print((i, j)) #, block, w[j:j + k])
                count += 1
                ww = w[j + 1:]
            else:
                break

        #block = cv[i:i + k]
        #if block in w:
        #    print((i, w.find(block)))

#    print(count)


if __name__ == '__main__':
    inp, out = small_example()
    #inp, out = big_example()
    inp = read_dataset()

    k = int(inp[0])
    v = Seq(inp[1])
    w = Seq(inp[2])

    #with open('example_result.txt') as f:
    #    print(len(f.readlines()))
    #with open('ex_res.txt', 'w') as f2:
    #    with open('example_result.txt') as f:
    #        vs = sorted(tuple(map(int, l.strip()[1:-1].split(', ')))
    #                    for l in f.readlines())
    #        for a, b in vs:
    #            f2.write(str((a, b)) + ' ' + str(v[a:a + k]) + ' ' + str(w[b:b + k]) + '\n')

    #print()

    syntenies(v, w, k)