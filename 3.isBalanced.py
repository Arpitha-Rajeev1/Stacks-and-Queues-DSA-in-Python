
from sys import stdin


def isBalanced(expression):
    s = []
    for char in expression:
        if char in '({[':
            s.append(char)
        elif char == ')':
            if(not s or s[-1] != '('):
                return False
            s.pop()
        elif char == '}':
            if(not s or s[-1] != '{'):
                return False
            s.pop()
        elif char == ']':
            if(not s or s[-1] != '['):
                return False
            s.pop()
    if (not s):
        return True
    return False


expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")
else:
    print("false")
