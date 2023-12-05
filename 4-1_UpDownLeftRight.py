
n = int(input()) #int를 안하면 str로 input받으며 type error
plans = input().split()

x, y = 1, 1

#L, R, U, D에 따른 이동방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue #nx, ny가 범위를 벗어나면 아래의 코드를 실행 x
    x, y = nx, ny

print(x, y)

"""
#step 방식으로 풀기
n = 5
plans = ["R", "R", "R", "U", "D", "D"]

row, column = 1, 1
move_types = ["L", "R", "U", "D"]
step = [(0,-1), (0,1), (-1, 0), (1,0)]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            next_row = row+ step[i][0]
            next_column = column +step[i][1]

            if next_row < 1 or next_row > n or next_column < 1 or next_column > n:
                continue
            row, column = next_row, next_column

print(row, column)
"""


"""
n = int(input()) #int를 안하면 str로 input받으며 type error
plan = input().split()

x, y = 1, 1

#if문으로 처리할 경우, 짧은 경우에는 편리하지만 조금만 복잡하면 구현 및 처리 속도에 문제가 생길 수 있음
for i in plan:
    if i == "L" and y-1 >= 1:
        y -= 1
    
    elif i == "R" and y+1 <= n:
        y += 1
    
    elif i == "U" and x-1 >= 1:
        x -= 1
    
    elif i == "D" and x+1 <= n:
        x += 1
    

print(x, y)
"""