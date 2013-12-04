codon_table = '''AAA K
AAC N
AAG K
AAU N
ACA T
ACC T
ACG T
ACU T
AGA R
AGC S
AGG R
AGU S
AUA I
AUC I
AUG M
AUU I
CAA Q
CAC H
CAG Q
CAU H
CCA P
CCC P
CCG P
CCU P
CGA R
CGC R
CGG R
CGU R
CUA L
CUC L
CUG L
CUU L
GAA E
GAC D
GAG E
GAU D
GCA A
GCC A
GCG A
GCU A
GGA G
GGC G
GGG G
GGU G
GUA V
GUC V
GUG V
GUU V
UAA 
UAC Y
UAG 
UAU Y
UCA S
UCC S
UCG S
UCU S
UGA 
UGC C
UGG W
UGU C
UUA L
UUC F
UUG L
UUU F'''

lines = [line.strip().split() for line in codon_table.split('\n')]

codon_map = dict(tuple(record) if len(record) == 2 else (record[0], '-') for record in lines)


def rc(dna):
    return dna[::-1].replace('A', '-')\
                    .replace('T', 'A')\
                    .replace('-', 'T')\
                    .replace('C', '-')\
                    .replace('G', 'C')\
                    .replace('-', 'G')


def codons_from_seq(seq):
    return [seq[i:i + 3] for i in range(0, len(seq), 1) if i + 3 <= len(seq)]


def transcribe(dna):
    return dna.replace('T', 'U')


def translate(codons):
    pairs = [(codon, codon_map.get(codon, '-')) for codon in codons]
    return ''.join([prot for codon, prot in pairs if '-' not in prot])


def find_in_dna(dna, ptn):
    for j in range(len(dna) - 3 * len(ptn) + 1):
        sub_dna = dna[j:j + len(ptn) * 3]
        codons = [sub_dna[i * 3:i * 3 + 3] for i in range(len(ptn))]
        # print codons, translate(codons)
        if j % 100000 == 0: print '!', j / 1000, 'kb'
        if ptn == translate(map(transcribe, codons)) or \
                        ptn == translate(map(transcribe, map(rc, codons[::-1]))):
            print ''.join(codons)

        # 2task: print '\n'.join(find_in_seq(dna, prt))

        # 1task: print ''.join([codon_map[codon] for codon in codons if codon_map[codon] is not None])

        # Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr

# print 4 * 2 * 6 * 2 * 4 * 1 * 2 * 2 * 2 * 2

# with open('dna.txt') as f:
# 	dna = f.read()
# ptn = 'VKLFPWFNQY'

# print 'dna len:', len(dna)
# find_in_dna(dna, ptn)

data = '''
Ala	A
Arg	R
Asn	N
Asp	D
Cys	C
Glu	E
Gln	Q
Gly	G
His	H
Ile	I
Leu	L
Lys	K
Met	M
Phe	F
Pro	P
Ser	S
Thr	T
Trp	W
Tyr	Y
Val	V
'''
# long_to_short_map = dict([a.split() for a in data.split('\n') if a])
# print ''.join([long_to_short_map[n] for n in 'Val-Lys-Leu-Phe-Pro-Trp-Phe-Asn-Gln-Tyr'.split('-')])

