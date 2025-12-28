import sys
input = sys.stdin.readline

s = input().rstrip()
boom_s = input().rstrip()

stack = []
boom_len = len(boom_s)

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-boom_len:]) == boom_s:
        for _ in range(boom_len):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')