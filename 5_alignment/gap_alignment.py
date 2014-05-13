from collections import defaultdict
from common import small_example, read_dataset, write_result
from itertools import count

def output_alignment(backtracks, v, w):
    back_vert, back_hori, back_diag = backtracks

    v_res = []
    w_res = []
    i = len(v)
    j = len(w)
    bt = back_diag

    while i > 0 or j > 0:
        if bt[i][j] == '↓':
            i -= 1
            v_res.append(v[i])
            w_res.append('-')
            bt = back_diag

        if bt[i][j] == '→':
            j -= 1
            v_res.append('-')
            w_res.append(w[j])
            bt = back_diag

        if bt[i][j] == 'v':
            bt = back_vert

        if bt[i][j] == 'h':
            bt = back_hori

        if bt[i][j] == '\\':
            i -= 1
            j -= 1
            v_res.append(v[i])
            w_res.append(w[j])

        if bt[i][j] == '|':
            i -= 1
            v_res.append(v[i])
            w_res.append('-')

        if bt[i][j] == '-':
            j -= 1
            v_res.append('-')
            w_res.append(w[j])

    print(''.join(v_res[::-1]))
    print(''.join(w_res[::-1]))

def global_alignment(v, w, scoring, gap_open, gap_ext):
    diag = [[-float('inf')] * (len(w) + 1) for _ in range(len(v) + 1)]
    delt = [[-float('inf')] * (len(w) + 1) for _ in range(len(v) + 1)]
    insr = [[-float('inf')] * (len(w) + 1) for _ in range(len(v) + 1)]
    back_diag = [['*'] * (len(w) + 1) for _ in range(len(v) + 1)]
    back_delt = [['*'] * (len(w) + 1) for _ in range(len(v) + 1)]
    back_insr = [['*'] * (len(w) + 1) for _ in range(len(v) + 1)]

    diag[0][0] = 0

    delt[0][0] = 0
    delt[1][0] = -gap_open
    for i in range(2, len(v) + 1):
        delt[i][0] = delt[i - 1][0] - gap_ext
        back_delt[i][0] = '|'

    insr[0][0] = 0
    insr[0][1] = -gap_open
    for j in range(2, len(w) + 1):
        insr[0][j] = insr[0][j - 1] - gap_ext
        back_insr[0][j] = '-'

    for i in range(len(v) + 1):
        for j in range(len(w) + 1):
            if i > 0:
                opts = [delt[i - 1][j] - gap_ext,
                        diag[i - 1][j] - gap_open]
                delt[i][j] = max(opts)
                back_delt[i][j] = {
                    opts[0]: '|',
                    opts[1]: '↓'
                }[delt[i][j]]

            if j > 0:
                opts = [insr[i][j - 1] - gap_ext,
                        diag[i][j - 1] - gap_open]
                insr[i][j] = max(opts)
                back_insr[i][j] = {
                    opts[0]: '-',
                    opts[1]: '→'
                }[insr[i][j]]

            if i > 0 and j > 0:
                opts = [delt[i][j],
                        insr[i][j],
                        diag[i - 1][j - 1] + scoring[v[i - 1]][w[j - 1]]]
                diag[i][j] = max(opts)
                back_diag[i][j] = {
                    opts[0]: 'v',
                    opts[1]: 'h',
                    opts[2]: '\\'
                }[diag[i][j]]

    #print('Deletions (gap in v):')
    #for l in back_delt: print(' '.join(l))
    #print('Insertions (gap in w):')
    #for l in back_insr: print(' '.join(l))
    #print('Matches/mismatches')
    #for l in back_diag: print(' '.join(l))
    #print('Deletions (gap in v):')
    #for l in delt: print(' '.join('{0:3}'.format(i) for i in l))
    #print('Insertions (gap in w):')
    #for l in insr: print(' '.join('{0:3}'.format(i) for i in l))
    #print('Matches/mismatches')
    #for l in diag: print(' '.join('{0:3}'.format(i) for i in l))
    return diag[len(v)][len(w)], (back_delt, back_insr, back_diag)


with open('scoring62.txt') as f:
    lines = f.readlines()

acids = lines[0].strip().split()
scoring = dict()
for acid1, line in zip(acids, lines[1:]):
    scoring[acid1] = dict()
    for acid2, value in zip(acids, map(int, line.split()[1:])):
        scoring[acid1][acid2] = value

inp, out = small_example()
inp = read_dataset()
#print(inp)
v, w = inp[0], inp[1]
#v, w = 'AGGC', 'AC'
l, backtrack = global_alignment(v, w, scoring, 8, 1)
print(l)
output_alignment(backtrack, v, w)
#print(out)