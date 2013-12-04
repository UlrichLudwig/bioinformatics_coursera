import operator
with open('integer_mass_table.txt') as f:
    mass_table = dict([(lambda c, w: (c, int(w)))(*line.split()) for line in f.readlines()])

#print mass_table

datasets = \
    [('LEQN', map(int, '0 113 114 128 129 227 242 242 257 355 356 370 371 484'.split())),
     ('IAQMLFYCKVATN', map(int, '0 71 71 99 101 103 113 113 114 128 128 131 147 163 170 172 184 199 215 227 227 231 244 259 260 266 271 286 298 298 310 312 328 330 330 372 385 391 394 399 399 399 401 413 423 426 443 443 470 493 498 502 513 519 526 527 541 554 556 557 564 569 590 598 616 626 640 654 657 658 665 670 682 697 697 703 711 729 729 753 753 771 779 785 785 800 812 817 824 825 828 842 856 866 884 892 913 918 925 926 928 941 955 956 963 969 980 984 989 1012 1039 1039 1056 1059 1069 1081 1083 1083 1083 1088 1091 1097 1110 1152 1152 1154 1170 1172 1184 1184 1196 1211 1216 1222 1223 1238 1251 1255 1255 1267 1283 1298 1310 1312 1319 1335 1351 1354 1354 1368 1369 1369 1379 1381 1383 1411 1411 1482'.split())),
     ]


def linear_spec(peptide):
    masses = []

    for l in range(1, len(peptide)):
        for i in range(len(peptide) - l + 1):
            subpep = peptide[i:i + l]
            mass = sum(subpep)
            masses.append(mass)
    masses.append(sum(peptide))
    return sorted(masses)


def generate_spec(peptide):
    masses = []

    for l in range(1, len(peptide)):
        for i in range(len(peptide)):
            subpep = (peptide + peptide[:-1])[i:i + l]
            mass = sum(subpep)
            masses.append(mass)
    masses.append(sum(peptide))
    return sorted(masses)


def get_mass(s):
    return sum(map(mass_table.get, s))


def test(n=1):
    seq = 'WLHLWKVDNVIHSRD'

    str_and_mass = [('', 0)]

    for l in range(1, len(seq)):
        for i in range(len(seq)):
            s = (seq + seq[:-1])[i:i + l]
            mass = get_mass(s)
            str_and_mass.append((s, mass))
    str_and_mass.append((seq, get_mass(seq)))

    real_spec = datasets[n][1]

    str_and_mass = sorted(str_and_mass, key=operator.itemgetter(1))

    mls = max(len(real_spec), len(str_and_mass))
    #print 'real got'
    #for i in range(mls):
    #    s, m = str_and_mass[i] if i < mls else ('-', '-')
    #    print (real_spec[i] if i < mls else '-'), m, s

    print ' '.join([str(m) for s, m in str_and_mass])

    #for i in range(len(real_spec)):
    #    if i < len(spec):
    #        spec.append(None)
    #    if real_spec[i] != spec[i]:
    #        print '\nspec[%d] = %d, real_spec[%d] = %d' % (i, spec[i], i, real_spec[i])
    #        return
    #    else:
    #        print spec[i],


#test(1)

    #print sum(map(mass_table.get, p)),