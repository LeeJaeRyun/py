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

ans_s = ""
for i in range(n):
    if length[i] == max_lcp:
        ans_s = arr[i][0]
        print(ans_s)
        target_prefix = ans_s[:max_lcp]
        for j in range(i+1, n):
            if arr[j][0][:max_lcp] == target_prefix:
                print(arr[j][0])
                sys.exit()