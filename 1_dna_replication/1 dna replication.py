dna = ''.join(open('Salmonella_enterica.fasta').read().split()[1:])


def most_frequent(dna, k, d):
    freqs = dict()
    acgt = {'A', 'C', 'G', 'T'}

    def f(l):
        if l == 0:
            return set()
        if l == 1:
            return {'A', 'C', 'G', 'T'}
        kmers = f(l - 1)
        new_kmers = set()
        for kmer in kmers:
            for c in 'ACGT':
                new_kmers.add(kmer + c)
        return new_kmers

    kmers = f(k)
    freqs = dict(zip(kmers, [0] * len(kmers)))

    def diff(c):
        return acgt - {c}

    def rc(dna):
        return dna[::-1].replace('A', '-')\
                        .replace('T', 'A')\
                        .replace('-', 'T')\
                        .replace('C', '-')\
                        .replace('G', 'C')\
                        .replace('-', 'G')

    def mutations(kmer, d):
        if d == 0:
            return {kmer}
        muts = mutations(kmer, d - 1)
        for mut in set(muts):
            for j in range(len(mut)):
                for c in acgt:
                    new_mut = mut[0:j] + c + mut[j + 1:]
                    muts.add(new_mut)
        return muts

    for i in range(len(dna) - k + 1):
        kmer = dna[i:i + k]
        for mut in mutations(kmer, d):
            freqs[mut] += 1
        for mut in mutations(rc(kmer), d):
            freqs[mut] += 1
        # print kmer, '->',
        # for j in range(len(kmer)):
        # 	for c in diff(kmer[j]):
        # 		km = kmer[0:j]+c+kmer[j+1:]
        # 		print km,
        # 		freqs[km] += 1
        # print

    max_freq = max(freqs.values())

    for kmer, freq in freqs.items():
        if freq >= max_freq - 3:
            print kmer, freq


# dna = open('Thermotoga-petrophila.txt').read()

# for i in range(len(s)-len(p)+1):
# 	if s[i:i+len(p)] == p:
# 		print i,

# dna = open('E-coli.txt').read()
# k, L, t = 9, 500, 3

# result = set()
# kmers = dict()
# kmers2 = []



# def check(kmer):
# 	num = kmers.get(kmer, 0) + 1
# 	kmers[kmer] = num
# 	if num == t:
# 		result.add(kmer)
# 	kmers2.append(kmer)

# for i in range(L - k + 1):
# 	check(dna[i:i + k])

# for i in range(0, len(dna) - L + 1):
# 	kmers[dna[i:i + k]] -= 1
# 	check(dna[i + L - k + 1:i + L + 1])

# print len(result)


def find_skew(dna):
    skews = [0]
    min_skew = 0
    for i, c in enumerate(dna):
        if i % 100000 == 0: print i / 1000, '000'
        skew = skews[-1]
        if c == 'C':
            skew -= 1
        if c == 'G':
            skew += 1
        skews.append(skew)
        min_skew = min(skew, min_skew)

    # print ' '.join(map(str, skews))
    print min_skew

    min_skew_positions = []
    for i, s in enumerate(skews):
        if s == min_skew:
            min_skew_positions.append(i)

    return min_skew_positions


def find_w_dist(pattern, dna, d):
    ii = 0
    for i in range(len(dna) - len(pattern) + 1):
        dist = 0
        for j in range(len(pattern)):
            if dna[i + j] != pattern[j]:
                dist += 1
        if dist <= d:
            print i,
            ii += 1
    print
    print ii

# print find_skew(dna)

min_skew_pos = 3764856  # 3764933

# most_frequent(dna[min_skew_pos-1000:min_skew_pos+1000], 9, 2)

find_w_dist('ATAAAAAAG', dna, 1)