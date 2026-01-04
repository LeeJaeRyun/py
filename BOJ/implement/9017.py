import sys
from collections import defaultdict
input = sys.stdin.readline


# 팀원 여섯명보다 작으면 계산에서 제외 (여섯명보다 많은 팀은 없음)
# 상위 4명의 점수를 합산해서 적은 팀이 이김
# 동점이면 다섯번째 선수 점수가 적은 팀이 이김

t = int(input())
for _ in range(t):
    n = int(input())
    result = list(map(int, input().split()))
    score = defaultdict(list)
    cnt = defaultdict(int)
    for team in result:
        cnt[team] += 1
    rank = 0
    for team in result:
        if cnt[team] == 6:
            rank += 1
            score[team].append(rank)
    team_score = {}
    for team in score:
        team_score[team] = sum(score[team][:4])
    winner = min(team_score.keys(), key = lambda x: (team_score[x], score[x][4]))
    print(winner)