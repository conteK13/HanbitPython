#경쟁적 전염

n, k = map(int, input().split())    #n 시험관의 크기, k 바이러스의 개수
data = []                           #시험관의 정보

for _ in range(n):
    data.append(list(map(int, input().split())))

s, result_x, result_y = map(int, input().split())       #result_x, y는 출력시 반드시 -1을 해줘야 함


virus = [[] for _ in range(k+1)]    #바이러스별 위치 

for x in range(n):
    for y in range(n):
        if data[x][y] != 0:         #바이러스가 있는 경우
            for i in range(1, k+1):   #바이러스 탐색
                if data[x][y] == i:
                    virus[i].append((x, y)) #virus 리스트에 바이러스의 위치 추가
                    break

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(s):
    for i in range(1, k+1):
        temp = []
        for x, y in virus[i]:
            for dx, dy in move:
                nx = x + dx
                ny = y + dy

                if nx>=0 and nx < n and ny >= 0 and ny < n:
                    if data[nx][ny]==0:
                        data[nx][ny] = i
                        temp.append((nx, ny))
        virus[i] = temp



print(data[result_x-1][result_y-1])
