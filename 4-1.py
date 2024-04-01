#상하좌우
"""
n = int(input())
move_data = list(input().split())
"""

n = 5
move_data = ['R','R', 'R', 'U', 'D', 'D']
now_x =1
now_y =1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ["L", "R", "U", "D"]
#x,y 좌표랑 row, colum의 개념이 헷갈림 주의


for i in (move_data):
    for j in range(len(move_type)):
        if i == move_type[j]:
            now_x += dx[j]
            now_y += dy[j]

            if now_x <= 0 or now_x > n or now_y <= 0 or now_y > n:
                now_x -= dx[j]
                now_y -= dy[j]
                #print("범위 벗어남")
            
            print(now_x, now_y)
            break

print(now_x, now_y)