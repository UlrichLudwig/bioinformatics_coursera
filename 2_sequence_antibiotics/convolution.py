#spec = map(int, '412 638 220 276 682 475 779 131 307 583 549 418 367 480 404 315 299 202 57 204 606 347 271 632 769 662 250 882 71 200 478 244 785 811 825 535 103 567 168 751 714 113 147 680 719 575 333 611 97 407 515 402 464 735 163 470 678 0'.split())
#
#for a1 in spec:
#    for a2 in spec:
#        if a2 > a1:
#            print a2 - a1,
#
spec = '57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493'

spec = sorted(map(int, spec.split()))

from leaderboard import get_score, fs

print get_score(fs('99-71-137-57-72-57'), spec)