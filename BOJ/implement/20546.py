import sys
input = sys.stdin.readline

money = int(input())
stock = list(map(int, input().split()))

jhMoney = money
smMoney = money
jhStock = 0
smStock = 0
for i in range(len(stock)):
    if jhMoney // stock[i] != 0:
        jhStock += jhMoney // stock[i]
        jhMoney -= (stock[i] * (jhMoney // stock[i]))
    else:
        continue
for i in range(3, 14):
    # 3일 연속 하락 → 매수
    if stock[i-3] > stock[i-2] > stock[i-1] > stock[i]:
        smStock += smMoney // stock[i]
        smMoney -= (smMoney // stock[i]) * stock[i]

    # 3일 연속 상승 → 매도
    elif stock[i-3] < stock[i-2] < stock[i-1] < stock[i]:
        smMoney += smStock * stock[i]
        smStock = 0

jhFinalMoney = stock[13] * jhStock + jhMoney
smFinalMoney = stock[13] * smStock + smMoney

if jhFinalMoney > smFinalMoney:
    print("BNP")
elif jhFinalMoney < smFinalMoney:
    print("TIMING")
else:
    print("SAMESAME")
