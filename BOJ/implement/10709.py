import sys
input = sys.stdin.readline

h, w = map(int, input().split())
test = []
for i in range(h):
    s = list(input().rstrip())
    test.append(s)

result = [[-1] * w for _ in range(h)]

for i in range(h):
    count = 0
    isMeetC = False
    for j in range(w):
        if test[i][j] == 'c':
            result[i][j] = 0
            count = 1
            isMeetC = True
        elif isMeetC:
            result[i][j] = count
            count += 1
for row in result:
    print(*row)
#이미 c를 만났을 경우 (지금 만난게 c라면 -> 그자리는 0 다음 자리는 1), (지금 만난게 c가 아니라면 -> 그 자리는 전꺼에 +1)
#c를 만나지 않은 경우 그자리는 원래값 그대로 -1