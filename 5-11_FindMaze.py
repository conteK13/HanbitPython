from collections import deque

n, m = map(int, input().split())    #n은 x(세로), m은 y(가로)

graph = []                          #한줄씩 노드 간 관계 입력     
for i in range(n):
    graph.append(list(map(int,input())))

#이동경로
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bsf(x, y):
    queue = deque()     #deque라이브러리 사용
    queue.append((x,y)) #queue에 첫 위치 입력

    while queue:
        x, y = queue.popleft()  #가장 왼쪽의 원소 출력

        for i in range(len(dx)): #예제 문제로 따지자면 for i in graph[v]
            nx = x+dx[i] 
            ny = y+dy[i]

            print("현재 위치", x, y)

            if nx <= -1 or nx >=n or ny <= -1 or ny >= m:   #범위를 벗어나면 for문 종료
                print(nx, ny, "범위를 벗어남")
                continue
            
            if graph[nx][ny] == 0:  #괴물을 만나면 for문 종료
                print(nx, ny, "진행할수 없는 곳")
                continue

            if graph[nx][ny] == 1:  #정상적인 길인 경우
                graph[nx][ny] = graph[x][y]+1   #이동 거리에 +1을 해준다
                print(nx, ny, "진행하겠음")
                queue.append((nx,ny)) #그리고 que에 값을 추가해줌
                print(queue)
                print(graph)
            
            else:
                print(nx, ny, "이미 가본 곳")

        print("진행중이던 queue 종료, 다음 queue 시작")

    return graph[n-1][m-1]      #종료지점 설정


x= bsf(0,0)
print(x)
