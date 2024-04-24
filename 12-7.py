#치킨 배달
#https://www.acmicpc.net/problem/15686

from itertools import combinations

#n, m = map(int, input().split())    #n 도시의 크기, m 남거둘 치킨 집 개수
#home, chicken = [], []

"""for r in range(n):
    data = list(map(int, input().split()))

    for c in range(n):
        if data[c] == 1:
            home.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))"""
n, m = 5, 2
home, chicken = [], []

data = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]

for r in range(n):
    for c in range(n):
        if data[r][c] == 1:
            home.append((r, c))
        elif data[r][c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))



def get_sum(candidate):
    result = 0
    for hx, hy in home:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+ abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))


print(result)