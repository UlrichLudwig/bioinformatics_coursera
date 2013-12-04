from subpeptides import generate_spec

with open('integer_mass_table.txt') as f:
    mass_by_acid = dict([(lambda c, w: (c, int(w)))(*line.split()) for line in f.readlines()])
acid_by_mass = dict([(m, s) for s, m in mass_by_acid.iteritems()])
masses = all_acids = sorted(list(set(mass_by_acid.values())))

spec = '97 99 113 114 128 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 388 389 ' \
       '390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 631 632 650 651 671 672 690 ' \
       '691 738 745 747 770 778 779 804 818 819 835 837 875 892 892 917 932 932 933 934 965 982 989 1031 ' \
       '1039 1060 1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322'
#spec = '0 113 114 128 129 227 242 242 257 355 356 370 371 484'
spec = sorted(map(int, spec.split()[1:]))


def brute_forse(spec):
    possible_spec_acids = [acid for acid in spec if acid in all_acids]
    desired_sum = spec[-1]
    max_len = len(possible_spec_acids)

    matches = []
    def combinate(peptides):
        next_peps = set()
        for peptide in peptides:
            if sum(peptide) == desired_sum:
                matches.append(peptide)
            if sum(peptide) < desired_sum and len(peptide) <= max_len:
                l = len(peptide)
                for acid in possible_spec_acids:
                    next_peps.add(peptide + (acid,))
        if next_peps:
            print l, len(next_peps)
            combinate(next_peps)

    combinate([(a,) for a in possible_spec_acids])

    print '\nMatches:', len(matches)
    for peptide in matches:
        test_spec = generate_spec(peptide)
        if test_spec == spec:
            print '-'.join(map(str, peptide)), ' ', \
                ''.join(map(acid_by_mass.get, peptide)), ' ', \
                ' '.join(map(str, test_spec))


#brute_forse(spec)


def check_duplicate_masses():
    for m1 in masses[:]:
        for m2 in masses[:]:
            sum2 = m1 + m2
            if sum2 < masses[-1]:
                if sum2 in masses:
                    print m1, '+', m2, '=', sum2, acid_by_mass[sum2]
#check_duplicate_masses()