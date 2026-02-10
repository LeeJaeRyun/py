# 숫자가 채워지는 패턴이 n**n 부터 시작해서 아래 → 오른쪽 → 위 → 왼쪽
import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

a = [[0]*n for _ in range(n)]

# 방향: 아래(0) → 오른쪽(1) → 위(2) → 왼쪽(3)
dr = [1,0,-1,0]
dc = [0,1,0,-1]

d = 0 # 현재 방향 | 현재 어느 방향으로 움직이고 있는지
r = c = 0 # 현재 위치 | r은 세로 위치(행), c는 가로 위치(열)

pos_r = pos_c = 0 # target 위치

for val in range(n*n, 0, -1):
    a[r][c] = val

    if val == target:
        pos_r, pos_c = r+1, c+1

    nr = r + dr[d]
    nc = c + dc[d]

    #지도 안이 아니거나 밟은게 아니라면
    if not (0 <= nr < n and 0 <= nc < n) or a[nr][nc] != 0:
        d = (d+1) % 4
        nr = r + dr[d]
        nc = c + dc[d]

    r, c = nr, nc

for row in a:
    print(*row)
print(pos_r, pos_c)
