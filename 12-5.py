#뱀

#사과를 먹으면 뱀의 길이가 늘어남
#벽이 부딪히거나 자기 자신에게 부딪히면 종료

"""n = int(input())
k = int(input())"""
n = 10
k = 5
graph =[[0] * (n+1) for _ in range(n+1)]

graph[1][2] =1
graph[1][3] =1
graph[1][6] =1
graph[1][7] =1
graph[1][5] =1

"""graph[3][4] =1
graph[2][5] = 1
graph[5][3] = 1"""

l = 4
info = [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
#info = [(3, 'D'), (15, 'L'), (17, 'D')]

"""for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

l = int(input())

info = []
for _ in range(l):
    a, b = input().split()
    info.append((int(a), b))"""

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]




def main(graph, info):
    direct = 0      #이동방향, L이면 -1, D면 +1
    index = 0       #info의 index
    time = 0        #총 게임 진행 시간
    snake= [(1,1)]  #뱀의 위치

    while True:
        time +=1
        x, y = snake[-1]
        nx = x + move[direct][0]
        ny = y + move[direct][1]

        #print(time, nx, ny)
        
        if nx <= 0 or nx > n or ny <= 0 or ny > n:
            return time
                
        if (nx, ny) in snake:
            return time

        snake.append((nx, ny))
        
        if graph[nx][ny] !=1:
            del snake[0]

        else:
            graph[nx][ny] -=1

        if index < l and time == info[index][0]:
            if info[index][1] == "L":
                direct -=1 
                if direct < 0:   direct += 3

            elif info[index][1] == "D":
                direct +=1 
                if direct > 3:   direct -= 3

            index += 1
    
    return time

result = main(graph, info)
print(result)


