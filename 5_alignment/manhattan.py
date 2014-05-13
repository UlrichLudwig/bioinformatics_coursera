from common import small_example, read_dataset


def manhattan_tourist(n, m, down, right):
    s = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        s[i + 1][0] = s[i][0] + down[i][0]

    for j in range(m):
        s[0][j + 1] = s[0][j] + right[0][j]

    for i in range(n):
        for j in range(m):
            s[i + 1][j + 1] = max(s[i][j + 1] + down[i][j + 1],
                                  s[i + 1][j] + right[i + 1][j])
    for l in s:
        print(l)
    return s[n][m]


inp = read_dataset()
n = int(inp[0])
m = int(inp[1])
down = [list(map(int, l.split())) for l in inp[2:2 + n]]
right = [list(map(int, l.split())) for l in inp[2 + n + 1:]]

print(manhattan_tourist(n, m, down, right))
#print(out)


def num_simple_ways():
    m = 12 + 1
    n = 16 + 1

    ways = [[0] * m for _ in range(n)]
    for i in range(n):
        ways[i][0] = 1
    for j in range(m):
        ways[0][j] = 1

    for i in range(n):
        print()
        for j in range(m):
            print(ways[i][j], end=' ')
    print()

    for i in range(1, n):
        for j in range(1, m):
            ways[i][j] = ways[i - 1][j] + ways[i][j - 1]

    for i in range(n):
        print()
        for j in range(m):
            print(ways[i][j], end=' ')
    print()

    print(ways[n - 1][m - 1])