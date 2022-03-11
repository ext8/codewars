# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

from collections import Counter

def find_uniq(z):
    x = ["".join(set(x.lower())) for x in z]
    return z[(x.index(min(Counter(x), key=Counter(x).get)))]
