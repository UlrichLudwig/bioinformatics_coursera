from subpeptides import linear_spec

with open('integer_mass_table.txt') as f:
    mass_by_acid = dict([(lambda c, w: (c, int(w)))(*line.split()) for line in f.readlines()])
acid_by_mass = dict([(m, s) for s, m in mass_by_acid.iteritems()])
masses = all_acids = sorted(list(set(mass_by_acid.values())))

spec = '0 97 99 113 114 128 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 388 389 ' \
       '390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 631 632 650 651 671 672 690 ' \
       '691 738 745 747 770 778 779 804 818 819 835 837 875 892 892 917 932 932 933 934 965 982 989 1031 ' \
       '1039 1060 1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322'
spec = '0 113 114 128 129 227 242 242 257 355 356 370 371 484'
spec = '0 113 128 186 241 299 314 427'
#spec = '0 97 97 99 101 103 196 198 198 200 202 295 297 299 299 301 394 396 398 400 400 497'
#spec = '0 97 97 99 103 196 198 198 201 202 295 297 299 300 301 394 396 398 400 400 497'

spec = sorted(map(int, spec.split()))


def consistent(spec, ref_spec):
    spec = sorted(spec)
    j = 0
    for acid in spec:
        while True:
            if j >= len(ref_spec) or ref_spec[j] > acid:
                return False
            if acid == ref_spec[j]:
                break
            j += 1
        j += 1
    return True


def sequence(spec):
    peptides = []

    with open('peptides.txt', 'w') as f:
        peps = [(0,)]
        while peps:
            pep = peps[0]
            peps = peps[1:]
            for mass in masses:
                next_pep = pep + (mass,)
                if next_pep == (0, 103, 99, 97):
                    pass
                new_spec = linear_spec(next_pep[1:])
                if sum(next_pep) == spec[-1]:
                    #f.write('-'.join(map(str, next_pep[1:])) + ' ')
                    peptides.append(next_pep[1:])
                elif consistent(new_spec, spec):
                    peps.append(next_pep)
                    #print next_pep

    print len(peptides)

    for p in peptides:
        print '-'.join(map(str, p))


sequence(spec)
