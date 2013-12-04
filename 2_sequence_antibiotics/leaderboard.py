from collections import defaultdict
from subpeptides import linear_spec, generate_spec
from heapq import heappush, heappop

with open('integer_mass_table.txt') as f:
    mass_by_acid = dict([(lambda c, w: (c, int(w)))(*line.split()) for line in f.readlines()])
acid_by_mass = dict([(m, s) for s, m in mass_by_acid.iteritems()])
acids = sorted(list(set(mass_by_acid.values())))

#spec = '0 71 113 129 147 200 218 260 313 331 347 389 460'
#spec = '0 71 97 101 103 113 113 113 113 114 114 115 128 128 128 128 129 131 131 131 156 156 184 186 186 200 214 227 227 228 230 231 241 242 242 243 244 244 256 257 262 269 270 287 298 299 301 328 331 340 340 343 345 345 356 358 359 370 370 372 375 383 385 397 400 401 429 430 442 453 454 454 459 462 468 471 472 473 474 485 486 487 498 499 501 512 514 514 542 561 567 570 573 575 581 583 585 590 599 600 600 601 602 610 615 615 616 627 627 630 658 695 696 698 698 698 701 703 704 713 723 728 728 728 728 730 730 731 741 744 747 758 761 769 799 810 817 827 829 831 832 841 841 844 844 851 854 854 857 859 862 872 882 884 886 889 928 928 944 945 947 955 955 958 959 960 966 967 972 972 982 985 990 996 997 1000 1000 1003 1041 1056 1059 1062 1068 1068 1068 1073 1075 1075 1084 1087 1089 1095 1097 1103 1113 1114 1128 1128 1131 1152 1172 1172 1181 1182 1184 1189 1190 1190 1196 1197 1199 1200 1202 1210 1212 1227 1231 1242 1259 1259 1283 1295 1298 1303 1303 1303 1303 1304 1311 1312 1317 1318 1325 1325 1328 1330 1338 1340 1345 1355 1356 1388 1396 1416 1426 1426 1427 1431 1432 1432 1434 1440 1442 1443 1445 1451 1453 1453 1454 1458 1459 1459 1469 1489 1497 1529 1530 1540 1545 1547 1555 1557 1560 1560 1567 1568 1573 1574 1581 1582 1582 1582 1582 1587 1590 1602 1626 1626 1643 1654 1658 1673 1675 1683 1685 1686 1688 1689 1695 1695 1695 1696 1701 1703 1704 1713 1713 1733 1754 1757 1757 1771 1772 1782 1788 1790 1796 1798 1801 1810 1810 1812 1817 1817 1817 1823 1826 1829 1844 1882 1885 1885 1888 1889 1895 1900 1903 1913 1913 1918 1919 1925 1926 1927 1930 1930 1938 1940 1941 1957 1957 1996 1999 2001 2003 2013 2023 2026 2028 2031 2031 2034 2041 2041 2044 2044 2053 2054 2056 2058 2068 2075 2086 2116 2124 2127 2138 2141 2144 2154 2155 2155 2157 2157 2157 2157 2162 2172 2181 2182 2184 2187 2187 2187 2189 2190 2227 2255 2258 2258 2269 2270 2270 2275 2283 2284 2285 2285 2286 2295 2300 2302 2304 2310 2312 2315 2318 2324 2343 2371 2371 2373 2384 2386 2387 2398 2399 2400 2411 2412 2413 2414 2417 2423 2426 2431 2431 2432 2443 2455 2456 2484 2485 2488 2500 2502 2510 2513 2515 2515 2526 2527 2529 2540 2540 2542 2545 2545 2554 2557 2584 2586 2587 2598 2615 2616 2623 2628 2629 2641 2641 2642 2643 2643 2644 2654 2655 2657 2658 2658 2671 2685 2699 2699 2701 2729 2729 2754 2754 2754 2756 2757 2757 2757 2757 2770 2771 2771 2772 2772 2772 2772 2782 2784 2788 2814 2885'
#spec = '0 97 99 114 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 385 389 390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 632 650 651 671 672 690 691 738 745 747 770 778 779 804 818 819 820 835 837 875 892 917 932 932 933 934 965 982 989 1030 1039 1060 1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322'
#spec = '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'
#spec = '57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'
spec = '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'

spec = sorted(map(int, spec.split()))


def ts(peptide):
    return '-'.join(map(str, peptide))


def fs(string):
    return map(int, string.split('-'))


def cut(leaderboard, spectrum, n):
    new_leaderboard = []
    i = 0
    tie_score = None
    while leaderboard:
        i += 1
        score, pep = heappop(leaderboard)
        if i == n:
            tie_score = score
        if i > n and score < tie_score:
            break
        heappush(new_leaderboard, (score, pep))

    return new_leaderboard


def get_score(peptide, ref_spec):
    spectrum = [0] + sorted(generate_spec(peptide))
    ref_spec = ref_spec[:]
    #print ' '.join(map(str, spectrum))
    #print ' '.join(map(str, ref_spec))
    score = 0
    i, j = 0, 0
    while i < len(spectrum) and j < len(ref_spec):
        if spectrum[i] == ref_spec[j]:
            #print spectrum[i],
            score += 1
            #print spectrum[i], ref_spec[j], '', score
            i += 1
            j += 1
        elif spectrum[i] < ref_spec[j]:
            #print spectrum[i], '   '
            i += 1
        elif spectrum[i] > ref_spec[j]:
            #print '   ', ref_spec[j]
            j += 1
    #print
    return score


def sequence(spectrum, n):
    matches = []
    leader = (0, (0,))
    leaderboard = []
    heappush(leaderboard, leader)
    parent = spectrum[-1]

    while leaderboard:
        peptide = heappop(leaderboard)[1]
        for acid in acids:
            new_peptide = peptide + (acid,) if peptide[0] else (acid,)
            new_score = get_score(new_peptide, spectrum)
            if sum(new_peptide) == parent:
                #print '-'.join(map(str, new_peptide)), '', new_score, '', sorted(generate_spec(new_peptide[1:]))
                matches.append((new_score, new_peptide))
                if new_score > leader[0]:
                    leader = new_score, new_peptide
            elif sum(new_peptide) < parent:
                heappush(leaderboard, (-new_score, new_peptide))
        leaderboard = cut(leaderboard, spectrum, n)

    return leader[1], matches


def expand(leaderboard, bitches):
    n_l = []
    for peptide in leaderboard[:]:
        for acid in bitches:
            new_peptide = peptide + (acid,) if peptide[0] else (acid,)
            n_l.append(new_peptide)
    return n_l


def cut_book(leaderboard, spectrum, n):
    sorted_lb = sorted(leaderboard, key=lambda pep: -get_score(pep, spectrum))
    res = sorted_lb[:n]
    if len(sorted_lb) > n:
        tie_score = get_score(sorted_lb[-1], spectrum)
        res.extend([e for e in sorted_lb[n:] if get_score(e, spectrum) == tie_score])
    return res


def convolutions(spectrum, m):
    bitches = defaultdict(lambda: 0)
    for a1 in spectrum:
        for a2 in spectrum:
            if 57 <= a2 - a1 <= 200:
                bitches[a2 - a1] += 1
    sorted_bitches = sorted(bitches.items(), key=lambda (bitch, num): -num)
    res = [bitch for bitch, num in sorted_bitches[:m]]
    if len(sorted_bitches) > m:
        tie_num = sorted_bitches[-1][1]
        res.extend([b for b, num in sorted_bitches[m:] if num == tie_num])
    return res


def sequence_book(spectrum, n, m):
    if spectrum[0] != 0:
        spectrum = [0] + spectrum
    bitches = convolutions(spectrum, m)

    matches = defaultdict(list)
    leader, leader_score = (0,), 0
    leaderboard = [leader]
    parent = spectrum[-1]
    while leaderboard:
        leaderboard = expand(leaderboard, bitches)
        next_leaderboard = []
        for peptide in leaderboard:
            if sum(peptide) == parent:
                score = get_score(peptide, spectrum)
                if score > leader_score:
                    leader, leader_score = peptide, score
                    print ts(peptide), '', score, '', ts(generate_spec(peptide))
                matches[score].append(peptide)
            if sum(peptide) < parent:
                next_leaderboard.append(peptide)
        leaderboard = next_leaderboard
        leaderboard = cut_book(leaderboard, spectrum, n)

    return leader, leader_score, matches


#print get_score(fs('156-71-113-114-131-156-113-101-129-128-128-114-128-103-97-131-131-113-131-113-128-115-128-113'), spec)
#print generate_spec(map(int, '156-71-113-114-131-156-113-101-129-128-128-114-128-103-97-131-131-113-131-113-128-115-128-113'.split('-')))
#print get_score(fs('113-147-71-129'), spec)
print
leader, leader_score, matches = sequence_book(spec, 100, 20)
print '\nLeader:', ts(leader), '', leader_score
print

#ref = fs('99-128-113-147-97-71-115-147-114-128-163')

for score, peps in sorted(matches.items())[::-1]:
    print score, len(peps)
    for pep in peps:
        print ts(pep),
    print
    print

i = 0
for score, peps in sorted(matches.items())[::-1]:
    for pep in peps:
        if i < 23:
            print ts(pep),
            i += 1


#a = '''113-128-99-163-128-114-147-71-115-97-147 113-128-99-163-128-114-147-115-71-97-147 114-128-163-99-128-113-147-97-71-115-147 147-114-128-163-99-128-113-147-97-71-115 97-147-113-128-99-163-128-114-147-71-115 147-113-128-99-163-128-114-147-71-115-97 128-99-163-128-114-147-71-115-97-147-113 71-115-147-114-128-163-99-128-113-147-97 147-113-128-99-163-128-114-147-115-71-97 128-99-163-128-114-147-115-71-97-147-113 147-114-128-163-99-128-113-147-97-115-71 97-147-113-128-99-163-128-114-147-115-71 128-114-147-115-71-97-147-113-128-99-163 163-128-114-147-115-71-97-147-113-128-99 97-147-113-128-99-163-128-57-57-147-71-115 97-147-113-128-99-163-128-57-57-147-115-71 114-128-163-99-71-57-113-147-97-71-115-147 147-114-128-163-99-71-57-113-147-97-115-71 147-114-128-163-99-71-57-113-147-97-71-115 147-113-128-99-163-128-57-57-147-71-115-97 163-128-114-147-115-71-97-147-113-57-71-99'''
#
#lines = a.split()
#print len(lines)
#
#cycles = defaultdict(list)
#for pep_str in lines:
#    #print pep_str,
#    pep = fs(pep_str)
#    found = False
#    for cycle, peps in cycles.iteritems():
#        if pep_str in cycle:
#            peps.append(pep)
#            found = True
#    if not found:
#        cycles[pep_str + '-' + pep_str] = [pep]
#
#print
#print
#print
#for cycle, peps in cycles.iteritems():
#    print '\n'.join(map(ts, peps))
#    print
#
#print
#print
#
#for cycle1 in cycles:
#    for cycle2 in cycles:
#        all_peps = [peps for c, peps in cycles.iteritems() if c != cycle1 and c != cycle2]
#        peps = []
#        for ps in all_peps:
#            peps.extend(ps)
#        if len(peps) == 14:
#            print ' '.join(map(ts, peps))
#        else:
#            print len(peps)
#        print

#print ts([mass_by_acid[a] for a in 'VKLFPADFNQY'])
















