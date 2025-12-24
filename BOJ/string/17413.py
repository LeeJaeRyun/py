import sys
input = sys.stdin.readline

s = input().rstrip()
result = [] #최종 결과
stack = [] #태그 밖에서 뒤집을 문자들 임시 저장
in_tag = False #지금 <>안인지 판단여부

for ch in s:
    if ch == '<':
        while stack:
            result.append(stack.pop())
        in_tag = True
        result.append(ch)
    elif ch == '>':
        in_tag = False
        result.append(ch)
    elif in_tag:
        result.append(ch)
    else:
        if ch == ' ':
            while stack:
                result.append(stack.pop())
            result.append(' ')
        else:
            stack.append(ch)
while stack:
    result.append(stack.pop())
print(''.join(result))