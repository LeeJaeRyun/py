import sys
input = sys.stdin.readline

s = input().rstrip()
idx = 0
n = 0

while idx < len(s):
    n += 1
    for ch in str(n):
        if idx < len(s) and ch == s[idx]:
            idx += 1
        if idx == len(s):
            break
print(n)