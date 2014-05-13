from common import small_example, read_dataset
from itertools import count

def output_lcs(backtrack, v, i, j):
    res = []
    while i > 0 or j > 0:
        if backtrack[i][j] == '|':
            i -= 1
        if backtrack[i][j] == '-':
            j -= 1
        if backtrack[i][j] == '\\':
            i -= 1
            j -= 1
            res.append(v[i])
    print(''.join(res[::-1]))

def lcs(v, w):
    s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]

    backtrack = [[''] * (len(w) + 1) for _ in range(len(v) + 1)]
    for i in range(len(v) + 1):
        backtrack[i][0] = '|'
    for j in range(len(w) + 1):
        backtrack[0][j] = '-'
    backtrack[0][0] = '*'

    for i, vi in zip(count(), v):
        for j, wj in zip(count(), w):
            s[i + 1][j + 1] = max(s[i][j + 1], s[i + 1][j])
            if vi == wj:
                s[i + 1][j + 1] = max(s[i + 1][j + 1], s[i][j] + 1)
            if s[i + 1][j + 1] == s[i][j + 1]:
                backtrack[i + 1][j + 1] = '|'
            elif s[i + 1][j + 1] == s[i + 1][j]:
                backtrack[i + 1][j + 1] = '-'
            elif s[i + 1][j + 1] == s[i][j] + 1:
                backtrack[i + 1][j + 1] = '\\'

    #for l in s:
    #    print(l)
    return s[len(v)][len(w)], backtrack


inp, out = small_example()
#inp = read_dataset()
#print(inp)
v, w = inp[0], inp[1]
score = inp[2:]
#v, w = 'AC', 'ACA'
l, backtrack = lcs(v, w)
print(l)
#for l in backtrack:
#    print(' '.join(l))
output_lcs(backtrack, v, len(v), len(w))
#print(out)