#!/usr/bin/env python3
"""
Knights of the Round Table - permutation method.

by pulsar 77


All solutions are generated as follows:
- Each knight is represented by a letter.
- Arthur (A), Lancelot (L), and Kay (K) can already be seated.
- We also know that Lionel (I), Bedivere (B), and Tristan (T)
sit next to each other, either as IBT or TBI.
- Other forbidden pairs are listed as two-letter strings.
- With Arthur, Lancelot, and Kay fixed, generate all permutations
of the other knights (keeping IBT or TBI together).
- Convert each permutation into a string.
- The solutions are the strings that contain no forbidden pairs.
"""
from itertools import permutations, chain


names = {
    'A': 'Arthur',
    'L': 'Lancelot',
    'I': 'Lionel',
    'B': 'Bedivere',
    'T': 'Tristan',
    'W': 'Gawain',
    'G': 'Gareth',
    'H': 'Galahad',
    'P': 'Perceval',
    'K': 'Kay'
}


def round_table_from_permutations():
    forbidden = [
        'WT', 'TW', 'LW', 'WL', 'WI', 'IW', 'GH', 'HG', 'GL', 'LG', 'GK', 'KG',
        'PH', 'HP', 'PL', 'LP', 'PI', 'IP', 'TL', 'LT', 'TP', 'PT', 'TK', 'KT',
        'HW', 'WH', 'HK', 'KH', 'IH', 'HI']
    perms1 = permutations(['IBT', 'W', 'G', 'H', 'P'])
    perms2 = permutations(['TBI', 'W', 'G', 'H', 'P'])
    arrangements = (''.join(['AL', *perm, 'K']) for perm in chain(perms1, perms2))
    solutions = (arr for arr in arrangements if not any(f in arr for f in forbidden))
    for n, solution in enumerate(solutions, 1):
        print(f"{n}. {', '.join(names[c] for c in solution)}")


if __name__ == "__main__":
    round_table_from_permutations()
