import sys
input = sys.stdin.readline

result = {}
n = int(input().rstrip())
for _ in range(n):
    s = input().rstrip()
    # .이후부터 나오는단어를 추출해서
    ext = s.split('.')[-1]
    #만약 이 단어가 result 딕셔너리에 없다면 ==1 해주고
    #이미 있다면 +=1
    if ext not in result:
        result[ext] = 1
    else:
        result[ext] += 1

#끝나면 result 오름차순 사전순으로 정렬해주면 끝
for ext in sorted(result):
    print(ext, result[ext])