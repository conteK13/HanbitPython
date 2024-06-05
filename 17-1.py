#플로이드

n = 5 #int(input())    #도시의 개수
m = 14 #int(input())    #버스의 개수
inf = int(1e9)
"""data = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split()) #a출발도시, b 도착도시, c 비용
    data[a][b] = min(data[a][b], c)"""

data = [
    [inf, inf, inf, inf, inf, inf], 
    [inf, inf, 2, 3, 1, 10], 
    [inf, inf, inf, inf, 2, inf], 
    [inf, 8, inf, inf, 1, 1], 
    [inf, inf, inf, inf, inf, 3], 
    [inf, 7, 4, inf, inf, inf]]

for i in range(n+1):
    data[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            data[i][j] = min(data[i][j], data[i][k]+data[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] == inf:
            print(0, end=' ')
        else:
            print(data[i][j], end = ' ')
    print()