from collections import defaultdict
from alignment import global_alignment
from common import small_example, read_dataset, write_result, big_example
from itertools import count

def way(v, w, scoring, indel):
    #print(v)
    #print(w)
    s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(1, len(v) + 1): s[i][0] = s[i - 1][0] + indel
    for j in range(1, len(w) + 1): s[0][j] = s[0][j - 1] + indel

    for i, vi in zip(count(), v):
        for j, wj in zip(count(), w):
            s[i + 1][j + 1] = max(
                s[i][j + 1] + indel,
                s[i + 1][j] + indel,
                s[i][j] + scoring[vi][wj])
    #for l in s: print(' '.join('{0:3}'.format(i) for i in l))
    #print('Result: %d' % s[len(v)][len(w)])
    #print()
    return s


def middle_node(vv, ww, scoring, indel):
    j = len(vv) // 2
    s1 = way(vv[:j], ww, scoring, indel)
    s2 = way(vv[j:][::-1], ww[::-1], scoring, indel)
    sums = list(map(sum, zip(s1[-1], s2[-1][::-1])))
    m = max(sums)
    i = [i for i, a in enumerate(list(sums)) if a == m][0]
    return j, i


def linear_space_alignment(v, w, scoring, indel):
    v_res = ''
    w_res = ''
    length = 0

    def find(v, w, v_res, w_res, length):
        if len(v) <= 1 or len(w) <= 1:
            l, bt = global_alignment.global_alignment(v, w, scoring, indel)
            v_al, w_al = global_alignment.output_alignment(bt, v, w)
            return v_res + v_al, w_res + w_al, length + l

        (_i, _j) = middle_node(v, w, scoring, indel)
        v_res, w_res, length = find(v[:_i], w[:_j], v_res, w_res, length)
        return find(v[_i:], w[_j:], v_res, w_res, length)

    v_res, w_res, length = find(w, v, v_res, w_res, length)

    print(length)
    #print()
    #print('Alignment:')
    print(w_res)
    print(v_res)

with open('scoring62.txt') as f:
    lines = f.readlines()

acids = lines[0].strip().split()
scoring = dict()
for acid1, line in zip(acids, lines[1:]):
    scoring[acid1] = dict()
    for acid2, value in zip(acids, map(int, line.split()[1:])):
        scoring[acid1][acid2] = value  # = 1 if acid1 == acid2 else -1

#inp, out = small_example()
#inp, out = big_example()
inp = read_dataset()
#print(inp)
w, v = inp[0], inp[1]
#v, w = 'AG', 'ACG'
linear_space_alignment(w, v, scoring, -5)
#output_alignment(backtrack, v, w)