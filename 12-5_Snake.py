n = int(input())        #보드의 크기
k = int(input())        #사과의 개수

board = [[0]* (n+1) for _ in range(n+1)]    #보드의 크기 설정
for _ in range(k):                          #사과가 있는 자리에 1을 설정한다.
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
info = []
for _ in range(l):
    a, b = input().split()
    info.append([int(a), b])

move = [(0,1), (1,0), (0,-1), (-1,0)]

def check(snake, n):
    now_x = snake[-1][0]
    now_y = snake[-1][1]
    
    if now_x >= 1 and now_x <= n and now_y >=1 and now_y <= n:
        for i in snake[:-1]:
            if snake[-1] == i:
                #print("충돌")
                return False
    else: 
        #print("Fail :", now_x, now_y)
        return False
    
    
        
    return True

def main_fuc():
    snake=[[1,1]]       #뱀의 시작점 설정
    time = 0            #시간
    now = 0
    index = 0

    while True:
        dx = move[now][0]                   #방향 설정
        dy = move[now][1]

        time += 1                       #전진할 때마다 시간 +1
        now_x = snake[-1][0]+dx
        now_y = snake[-1][1]+dy
        snake.append([now_x, now_y])
        print(snake, board[now_x][now_y])

        if check(snake, n) == False:
            return time
        if board[now_x][now_y] == 1:    #오류가 났던 부분! 이미 먹은 사과는 0으로 바꿔야 한다
            board[now_x][now_y] = 0
        else:
            del snake[0]

            
        if index < l and time == info[index][0]:        #index < l을 잊지 말것!
            if info[index][1] == "D":    #오른쪽으로 회전
                now +=1
                if now >3: now -=4

            elif info[index][1] == "L":  #왼쪽으로 회전
                now -=1
                if now <0: now +=4
            index +=1
    
    return time
    
result = main_fuc()

print(result)

