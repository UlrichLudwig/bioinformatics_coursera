from collections import defaultdict
from math import log
M = '''T   C   G   G   G   G   g   T   T   T   t   t
   c   C   G   G   t   G   A   c   T   T   a   C
   a   C   G   G   G   G   A   T   T   T   t   C
   T   t   G   G   G   G   A   c   T   T   t   t
   a   a   G   G   G   G   A   c   T   T   C   C
   T   t   G   G   G   G   A   c   T   T   C   C
   T   C   G   G   G   G   A   T   T   c   a   t
   T   C   G   G   G   G   A   T   T   c   C   t
   T   a   G   G   G   G   A   a   c   T   a   C
   T   C   G   G   G   t   A   T   a   a   C   C'''

values = [l.split() for l in M.upper().split('\n')]

def entropy(column):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for c in column:
        counts[c] += 1
    for c in counts.keys():
        counts[c] = float(counts[c]) / float(len(column))
    ent = -sum([v * log(v, 2) if v > 0 else 0 for v in counts.values()])
    return ent

columns = [None] * len(values[0])
for row in range(len(values)):
    for col in range(len(values[row])):
        if columns[col] is None: columns[col] = []
        columns[col].append(values[row][col])

for column in columns:
    print entropy(column)

print
print sum(entropy(col) for col in columns)