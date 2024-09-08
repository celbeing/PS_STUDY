#1918: 후위 표기식
import sys
input = sys.stdin.readline

def solution():
    formula = list(input().rstrip())
    result = ""
    stack = []
    for f in formula:
        if f.isalpha():
            result += f
        elif f == "(":
            stack.append(f)
        elif f == "*" or f == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(f)
        elif f == "+" or f == "-":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(f)
        elif f == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
    while stack:
        result += stack.pop()
    print(result)
solution()