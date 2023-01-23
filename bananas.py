"""
Given a string of letters a, b, n how many different ways can you make the word "banana" by crossing out various letters and then reading left-to-right?
(Use - to indicate a crossed-out letter)
https://www.codewars.com/kata/5917fbed9f4056205a00001e
"""

from itertools import combinations


def bananas(s, pattern = "banana"):
    result = set()
    for c in combinations(range(len(s)), len(s) - len(pattern)):
        tmp = list(s)
        for i in c: tmp[i] = '-'
        tmp = ''.join(tmp)
        if tmp.replace('-', '') == pattern: result.add(tmp)
    return result

for i in bananas(input("Введите строку: ")): print(i)
