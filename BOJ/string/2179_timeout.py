import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for i in range(n):
    arr.append(input().rstrip())

answerMaxLength = 0 # 지금까지 찾은 공통 접두사의 최대 길이
answerTwoWord = [] # 최대 길이를 가진 두 단어 저장용 리스트

for i in range(n):
    for j in range(i+1, n):
        s1 = arr[i]
        s2 = arr[j]
        minL = min(len(s1),len(s2)) # 두 단어 중 짧은 단어 길이까지만 비교해야 인덱스 에러 안남
        maxL = 0 # 이 쌍에서 발견한 공통 길이
        length = 0 # 실제 일치하는 글자 수 카운트
        for k in range(minL):
            if s1[k] != s2[k]:
                maxL = max(maxL, length)
                break
            else:
                length += 1
        if length == minL:
            maxL = max(maxL,length)
        if answerMaxLength < maxL:
            answerTwoWord = [s1, s2]
            answerMaxLength = maxL

for i in range(2):
    print(answerTwoWord[i])


# 시간초과! 지금처럼 이중반복문으로 하면 시간 초과가 남
# 이걸 해결하기 위해서는 단어를 사전순으로 정렬하고 시작해야함. 공통 접두사가 비슷한 단어들끼리 서로 옆에 위치하니까
# 모든 쌍을 비교할 필요 없이 옆의 단어끼리만 비교하면 됌