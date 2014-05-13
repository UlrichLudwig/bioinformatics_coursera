from collections import defaultdict
from common import small_example, read_dataset, write_result
from itertools import count

def output_alignment(backtrack, v, w, pos):
    v_res = []
    w_res = []
    i, j = len(v) , pos
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
        if backtrack[i][j] == '*':
            i = 0
            j = 0
    print(''.join(v_res[::-1]))
    print(''.join(w_res[::-1]))

def fitting_alignment(v, w, scoring, indel):
    s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]

    backtrack = [[''] * (len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(1, len(v) + 1):
        s[i][0] = 0
        backtrack[i][0] = '*'

    for j in range(1, len(w) + 1):
        s[0][j] = j * indel
        backtrack[0][j] = '-'

    backtrack[0][0] = '*'

    max_pos_w, max_l = 0, 0

    for i, vi in zip(count(), v):
        for j, wj in zip(count(), w):
            opts = [
                s[i][j] + scoring[vi][wj],
                s[i][j + 1] + indel,
                s[i + 1][j] + indel,
                #0
            ]
            s[i + 1][j + 1] = max(opts)

            if s[i + 1][j + 1] > max_l and i == len(v) - 1:
                max_l = s[i + 1][j + 1]
                max_pos_w = j + 1

            backtrack[i + 1][j + 1] = {
                opts[0]: '\\',
                opts[1]: '|',
                opts[2]: '-',
                #opts[3]: '*'
            }[s[i + 1][j + 1]]

    #print('\n'.join(''.join('{0:3}'.format(d) for d in l) for l in s))

    return max_l, max_pos_w, backtrack


with open('scoring250.txt') as f:
    lines = f.readlines()

acids = lines[0].strip().split()
scoring = dict()
for acid1, line in zip(acids, lines[1:]):
    scoring[acid1] = dict()
    for acid2, value in zip(acids, map(int, line.split()[1:])):
        scoring[acid1][acid2] = 1 if acid1 == acid2 else -2  # value

inp, out = small_example()
inp = read_dataset()
#print(inp)
v, w = inp[0], inp[1]
#v, w = 'AC', 'ACA'
l, pos, backtrack = fitting_alignment(v, w, scoring, -2)
print(l)
#for l in backtrack:
#    print(''.join(l))
output_alignment(backtrack, v, w, pos)
#print(out)