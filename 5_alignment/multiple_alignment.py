from collections import defaultdict
from common import small_example, read_dataset, write_result
from itertools import count

def output_alignment(backtrack, v, w, u):
    v_res = []
    w_res = []
    u_res = []
    i = len(v)
    j = len(w)
    k = len(u)
    while i > 0 or j > 0 and k > 0:
        a, b, c = backtrack[i][j][k]
        if a == 1:
            i -= 1
            v_res += v[i]
        else:
            v_res += '-'

        if b == 1:
            j -= 1
            w_res += w[j]
        else:
            w_res += '-'

        if c == 1:
            k -= 1
            u_res += u[k]
        else:
            u_res += '-'

    return ''.join(v_res[::-1]), \
           ''.join(w_res[::-1]), \
           ''.join(u_res[::-1])

def alignment(v, w, u):
    s = [[[0] * (len(u) + 1)
          for _ in range(len(w) + 1)]
         for _ in range(len(v) + 1)]
    print(s)

    backtrack = [[[(None, None, None)] * (len(u) + 1)
                  for _ in range(len(w) + 1)]
                 for _ in range(len(v) + 1)]

    backtrack[0][0][0] = 0, 0, 0

    for i in range(1, len(v) + 1):
        s[i][0][0] = 0
        backtrack[i][0][0] = 1, 0, 0

    for j in range(1, len(w) + 1):
        s[0][j][0] = 0
        backtrack[0][j][0] = 0, 1, 0

    for k in range(1, len(u) + 1):
        s[0][0][k] = 0
        backtrack[0][0][k] = 0, 0, 1

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            s[i][j][0] = 0
            backtrack[i][j][0] = 1, 1, 0

    for j in range(1, len(w) + 1):
        for k in range(1, len(u) + 1):
            s[0][j][k] = 0
            backtrack[0][j][k] = 0, 1, 1

    for i in range(1, len(v) + 1):
        for k in range(1, len(u) + 1):
            s[i][0][k] = 0
            backtrack[i][0][k] = 1, 0, 1

    for i, vi in zip(count(), v):
        for j, wj in zip(count(), w):
            for k, uk in zip(count(), u):
                opts = [
                    s[i + 1][j + 1][k],
                    s[i + 1][j][k + 1],
                    s[i][j + 1][k + 1],
                    s[i + 1][j][k],
                    s[i][j + 1][k],
                    s[i][j][k + 1],
                    s[i][j][k] + 1 if (vi == wj == uk) else 0
                ]
                s[i + 1][j + 1][k + 1] = max(opts)

                backtrack[i + 1][j + 1][k + 1] = {
                    opts[0]: (0, 0, 1),
                    opts[1]: (0, 1, 0),
                    opts[2]: (1, 0, 0),
                    opts[3]: (0, 1, 1),
                    opts[4]: (1, 0, 1),
                    opts[5]: (1, 1, 0),
                    opts[6]: (1, 1, 1),
                }[s[i + 1][j + 1][k + 1]]

    #for l in s:
    #    print(' '.join('{0:3}'.format(i) for i in l))
    return s[len(v)][len(w)][len(u)], backtrack


if __name__ == '__main__':
    inp, out = small_example()
    inp = read_dataset()
    #print(inp)
    v, w, u = inp[0], inp[1], inp[2]
    #v, w = 'AC', 'ACA'
    l, backtrack = alignment(v, w, u)
    print(l)
    #for l in backtrack:
    #    print(' '.join(l))
    print('\n'.join(output_alignment(backtrack, v, w, u)))
    #print(out)