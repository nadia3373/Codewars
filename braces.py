from collections import deque


def valid_braces(string):
    stack = deque()
    for i in string:
        if i in ("(", "{", "["): stack.append(i)
        elif i in (")", "}", "]"):
            if not stack: return False
            else: tmp = stack.pop()
            print(i == "(" and tmp != ")")
            print(i == "{" and tmp != "}")
            print(i == "[" and tmp != "]")
            if (i == "(" and tmp != ")") or (i == "{" and tmp != "}") or (i == "[" and tmp != "]"): return False
    return True

valid_braces("(((({{")