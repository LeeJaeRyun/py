from collections import Counter

name = list(map(str,input())) #문자열을 문자 하나씩 리스트로 변환
name.sort() #오름차순 정렬
count = Counter(name) #각 문자 개수를 딕셔너리 형태로 저장
odd = 0 #홀수 개 문자 개수
odd_alpha = '' #홀수 개 문자를 가진 알파벳
ans = '' #팰린드롬의 왼쪽 절반

for i in count: #알파벳 하나씩 A->B->C 순으로
	if count[i] % 2 != 0: #홀수 개수 문자 체크: 홀수일 경우 실행
		odd += 1
		odd_alpha += i

	for _ in range(count[i]//2):  #왼쪽 절반 만들기: 해당 문자의 절반만 앞쪽에 배치 A가 4개면 앞에 2개를 배치
		ans += i

if odd > 1: #홀수 개 문자가 2개 이상이면 팰린드롬 못만듦
	print("I'm Sorry Hansoo")

elif odd == 0: #홀수 개 문자가 없는 경우
	print(ans + ans[::-1]) #완전 대칭 구조

else: #홀수 개 문자가 1개 있는 경우
	print(ans + odd_alpha + ans[::-1]) #홀수 문자는 가운데 배치

#팰린드롬의 조건
#1. 모든 문자 마다의 개수가 짝수개여야 함
#2. 문자열 길이가 홀수일 때 딱 하나의 문자만 홀수개가 가능
#3. 좌우대칭이어야하기 때문임