"""
Valid Braces
DESCRIPTION:
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid
This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.
https://www.codewars.com/kata/5277c8a221e209d3f6000b56
"""

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