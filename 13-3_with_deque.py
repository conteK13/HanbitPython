#13-3_with_deque
#경쟁적 전염

from collections import deque

n, k = map(int, input().split())    #n 시험관의 크기, k 바이러스의 개수
data = []                           #시험관의 정보
virus = []                          #바이러스의 정보
for i in range(n):
    data.append(list(map(int, input().split())))

    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j], 0, i, j))

target_s, target_x, target_y = map(int, input().split())       #result_x, y는 출력시 반드시 -1을 해줘야 함

virus.sort()
q= deque(virus)

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0

while q:
    index, t, x, y = q.popleft()

    if t == target_s:
        break

    for dx, dy in move:
        nx = x+dx
        ny = y+dy

        if nx>=0 and nx < n and ny >= 0 and ny < n:
            if data[nx][ny]==0:
                data[nx][ny] = index
                q.append((index, t+1, nx, ny))



print(data[target_x-1][target_y-1])