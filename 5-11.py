#미로 탈출
from collections import deque

"""n,m = map(int, input().split())
data =[]
for _ in range(n):
    data.append(list(map(int, input())))
"""

"""n, m = 3, 3
data = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]"""

n,m = 5,6
data = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 1

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >= 0 and ny < m and ny >= 0:
                if data[nx][ny] == 1:
                    q.append((nx,ny))
                    data[nx][ny] = data[x][y] +1      
    
bfs(0,0)
result = data[(n-1)][(m-1)]
print(result)