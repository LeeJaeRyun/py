import sys
input = sys.stdin.readline

n,m = list(map(int, input().split()))
result = {}
for _ in range(n):
    s = input().rstrip()
    if len(s) < m:
        continue
    else:
        if s in result:
            result[s] += 1
        else:
            result[s] = 1
result = sorted(result.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in result:
    print(i[0])