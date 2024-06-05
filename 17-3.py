#화성 탐사
import heapq
import sys
input = sys.stdin.readline
inf = 1e9

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


t = int(input())    #TC의 개수

for _ in range(t):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
        
    result = [[inf]*n for _ in range(n)]
    result[0][0] = data[0][0]

    x, y = 0, 0
    q = [(data[x][y], x, y)]

    while q:
        dist, x, y = heapq.heappop(q)

        if result[x][y] < dist:
            continue
        
        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue

            cost = dist + data[nx][ny]

            if cost < result[nx][ny]:
                result[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(result[n-1][n-1])