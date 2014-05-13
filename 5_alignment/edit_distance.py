from common import read_dataset, small_example

def edit_dist(v, w):
    dists = [[i + j for j in range(len(w))] for i in range(len(v))]
    dists[0][0] = 0

    for i in range(1, len(v)):
        for j in range(1, len(w)):
            dists[i][j] = min(
                dists[i - 1][j] + 1,
                dists[i][j - 1] + 1,
                dists[i - 1][j - 1] + (
                    1 if v[i - 1] != w[j - 1] else 0))

    print('\n'.join(' '.join(str(d) for d in l) for l in dists))
    return dists[len(v) - 1][len(w) - 1]

inp, out = small_example()
#inp = 'ABA', 'ABC'
inp = read_dataset()
print(inp)
v, w = inp[0], inp[1]
print(edit_dist(v, w))