import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for i in range(n):
    arr.append([input().rstrip(), i])
sorted_arr = sorted(arr)

length = [0] * n

max_lcp = 0
for i in range(n-1):
    s1, idx1 = sorted_arr[i]
    s2, idx2 = sorted_arr[i+1]
    count = 0
    for k in range(min(len(s1), len(s2))):
        if s1[k] == s2[k]:
            count += 1
        else:
            break
    if count > max_lcp:
        max_lcp = count
    length[idx1] = max(length[idx1], count)
    length[idx2] = max(length[idx2], count)

cnt = 0
for i in range(n):
    if cnt == 2:
        break
    if length[i] == max_lcp:
        print(arr[i][0])
        cnt += 1

# 이게 안되는 반례:
# 4
# aaX
# bbX
# aaY
# bbY
# 단순히 공통 접두사 길이만으로 앞에서부터 선착 두 개로 카운트 해버리면 aaX와 bbX가 출력되는 반례가 있음.