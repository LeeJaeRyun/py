import sys
input = sys.stdin.readline

n = int(input())
count = 0
cow = [-1] * 11
for _ in range(n):
    num, position = map(int, input().split())
    if cow[num] == -1:
        cow[num] = position
    elif cow[num] != position:
        cow[num] = position
        count += 1
print(count)
