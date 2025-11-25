word = input()
word = word.lower()
alpha = [0] * 26

for i in word:
    alpha[ord(i)-97] += 1

maxNum = max(alpha)

if alpha.count(maxNum) > 1:
    print('?')
else:
    print(chr(97+alpha.index(maxNum)).upper())