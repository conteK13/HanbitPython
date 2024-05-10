#블록 이동하기
#https://school.programmers.co.kr/learn/courses/30/lessons/60063


from collections import deque

def get_next(pos, board):
    next_pos = []
    pos= list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]     #좌표 1, 2의 위치를 가져온다

    #상하좌우 이동하는 경우의 수
    dx = [0, 1, 0, -1]      
    dy = [1, 0, -1, 0]
    
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]

        if board[nx1][ny1] == 0 and board[nx2][ny2] ==0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})

    #회전하는 경우의 수
    if x1 == x2:    #가로로 놓인 경우의 수
        for i in [-1, 1]:   #위, 아래 방향으로 회전
            if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                next_pos.append({(x1, y1), (x1+i, y1)})
                next_pos.append({(x2, y2), (x2+i, y2)})
    elif y1 == y2:  #세로로 놓인 경우
        for i in [-1, 1]:
            if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                next_pos.append({(x1, y1), (x1, y1+i)})
                next_pos.append({(x2, y2), (x2, y2+i)})
    return next_pos

def solution(board):
    n = len(board)  #board의 크기

    new_board = [[1] * (n+2) for _ in range(n+2)]   #외곽에 벽을 두는 새로운 board 생성(기본값 1)
    for x in range(n):
        for y in range(n):
            new_board[x+1][y+1] = board[x][y]

    q = deque()
    visited = []
    pos = {(1,1), (1,2)}    #시작위치를 집합으로 설정
    q.append((pos, 0))      #큐에 시작위치 삽입
    visited.append(pos)     #방문 처리

    while q:
        pos, cost = q.popleft()

        if (n, n) in pos:       #(n,n)에 도착하면 종료
            return cost
    
        for next_pos in get_next(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    
    return 0    #q의 모든 값을 처리하더라도 (n, n)에 도달하지 못할 경우

board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0,]
]

result = solution(board)

print(result)