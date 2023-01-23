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
