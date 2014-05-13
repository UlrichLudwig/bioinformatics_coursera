from collections import defaultdict
from common import small_example, read_dataset, write_result
from itertools import count

def output_alignment(backtrack, v, w):
    v_res = []
    w_res = []
    i = len(v)
    j = len(w)
    while i > 0 or j > 0:
        if backtrack[i][j] == '|':
            i -= 1
            v_res.append(v[i])
            w_res.append('-')
        if backtrack[i][j] == '-':
            j -= 1
            v_res.append('-')
            w_res.append(w[j])
        if backtrack[i][j] == '\\':
            i -= 1
            j -= 1
            v_res.append(v[i])
            w_res.append(w[j])
    return ''.join(v_res[::-1]), ''.join(w_res[::-1])

def global_alignment(v, w, scoring, indel):
    s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]

    backtrack = [[''] * (len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(1, len(v) + 1):
        s[i][0] = s[i - 1][0] + indel
        backtrack[i][0] = '|'

    for j in range(1, len(w) + 1):
        s[0][j] = s[0][j - 1] + indel
        backtrack[0][j] = '-'

    backtrack[0][0] = '*'

    for i, vi in zip(count(), v):
        for j, wj in zip(count(), w):
            opts = [
                s[i][j + 1] + indel,
                s[i + 1][j] + indel,
                s[i][j] + scoring[vi][wj]
            ]
            s[i + 1][j + 1] = max(opts)

            backtrack[i + 1][j + 1] = {
                opts[0]: '|',
                opts[1]: '-',
                opts[2]: '\\'
            }[s[i + 1][j + 1]]

    #for l in s:
    #    print(' '.join('{0:3}'.format(i) for i in l))
    return s[len(v)][len(w)], backtrack


if __name__ == '__main__':
    with open('scoring62.txt') as f:
        lines = f.readlines()

    acids = lines[0].strip().split()
    scoring = dict()
    for acid1, line in zip(acids, lines[1:]):
        scoring[acid1] = dict()
        for acid2, value in zip(acids, map(int, line.split()[1:])):
            scoring[acid1][acid2] = value

    inp, out = small_example()
    #inp = read_dataset()
    #print(inp)
    v, w = inp[0], inp[1]
    #v, w = 'AC', 'ACA'
    l, backtrack = global_alignment(v, w, scoring, -5)
    print(l)
    #for l in backtrack:
    #    print(' '.join(l))
    output_alignment(backtrack, v, w)
    #print(out)