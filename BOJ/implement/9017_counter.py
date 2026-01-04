import sys
from collections import defaultdict, Counter
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    result = list(map(int, input().split()))

    cnt = Counter(result)

    score = defaultdict(list)
    rank = 0

    for team in result:
        if cnt[team] == 6:
            rank += 1
            score[team].append(rank)

    team_score = {}
    for team in score:
        team_score[team] = sum(score[team][:4])

    winner = min(team_score.keys(),
                 key=lambda x: (team_score[x], score[x][4]))
    print(winner)