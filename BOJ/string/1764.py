n, m = list(map(int, input().split()))
x = set()
y = set()
result = []
for _ in range(n):
    x.add(input())
for _ in range(m):
    y.add(input())
for i in x:
    if i in y:
        result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)