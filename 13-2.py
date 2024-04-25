#연구소

n, m = map(int, input().split())    #n 세로크기, m 가로 크기 
graph = []
temp = [[0] *m for _ in range(n)]   #바이러스가 퍼진 경우의 수를 계산하기 위한 리스트

for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0

def virus(graph, x, y):
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if graph[x][y] == 2:    #바이러스가 있는 위치
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx >=0 and nx < n and ny >= 0 and ny < m:    #nx, ny가 범위 내
                if graph[nx][ny] == 0:                      #nx, ny가 빈공간이라면
                    graph[nx][ny] = 2
                    virus(graph, nx, ny)

def check(graph):
    result = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                result +=1
    return result

def dfs(index):
    global result
    if index == 3: #울타리를 3개 설치하면
        for x in range(n):
            for y in range(m):
                temp[x][y] = graph[x][y]
        
        for x in range(n):
            for y in range(m):
                if temp[x][y] ==2:
                    virus(temp, x, y)

        result = max(result, check(temp))
        return 
    
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                graph[x][y] =1
                index +=1       #울타리 개수
                dfs(index)
                graph[x][y] =0  #dfs가 끝나면 원복
                index -=1


dfs(0)
print(result)