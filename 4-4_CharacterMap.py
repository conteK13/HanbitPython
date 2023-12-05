n, m = map(int, input().split()) #세로 n, 가로 m
a, b, d = map(int, input().split()) #x좌표 a, y좌표 b, 방향 d

direction = [0, 1, 2, 3] # 북, 동, 남, 서
da = [-1, 0, 1, 0] #x값의 변화는 행의 변화
db = [0, 1, 0, -1] #y값의 변화는 열의 변화
#혼돈 주의!!!

#맵정보
map_array = []
for i in range(n): #세로 n만큼 반복
    map_array.append(list(map(int, input().split())))


#방문여부 List comprehension(괄호 안에 어떤 수식을 적더라도 리스트로 감싸안아준다) 사용
v = [[0]*m for _ in range(n)] #가로 m, 세로 n주의 
v[a][b] = 1 #현재위치 방문으로 변경


def turn_left():
    global d 
    d -= 1 #방향 d가 함수 바깥에서 선언된 전역변수
    if d == -1:
        d= 3

turn_time = 0
count =1 # 방문한 칸의 갯수이므로 현재 위치도 포함해야 함

while True:
    turn_left()
    
    na = a + da[d]
    nb = b + db[d]

    if v[na][nb] == 0 and map_array[na][nb] == 0: #방문한적 없고, 육지인 경우
        v[na][nb] =1
        a= na
        b= nb
        turn_time = 0
        count +=1
        continue

    else:
        turn_time +=1
    
    if turn_time == 4:
        na = a - da[d]
        nb = b - db[d]

        if map_array[na][nb] == 0:
            a = na
            b = nb
            turn_time = 0
        
        else:
            break

print(count)

"""
n, m = map(int, input().split()) #세로 n, 가로 m
a, b, d = map(int, input().split()) #x좌표 a, y좌표 b, 방향 d

direction = [0, 1, 2, 3] # 북, 동, 남, 서
step = [(-1,0), (0,1), (1, 0), (0,-1)]
#혼돈 주의!!!

#맵정보
map_array = []
for i in range(n): #세로 n만큼 반복
    map_array.append(list(map(int, input().split())))


#방문여부 List comprehension(괄호 안에 어떤 수식을 적더라도 리스트로 감싸안아준다) 사용
v = [[0]*m for _ in range(n)] #가로 m, 세로 n주의 
v[a][b] = 1 #현재위치 방문으로 변경


def turn_left():
    global d
    d -= 1 #방향 d가 함수 바깥에서 선언된 전역변수
    if d == -1:
        d= 3

turn_time = 0
count =1 # 방문한 칸의 갯수이므로 현재 위치도 포함해야 함

while True:
    turn_left()
    
    na = a + step[d][0]
    nb = b + step[d][1]

    if v[na][nb] == 0 and map_array[na][nb] == 0: #방문한적 없고, 육지인 경우
        v[na][nb] =1
        a= na
        b= nb
        turn_time = 0
        count +=1
        continue

    else:
        turn_time +=1
    
    if turn_time == 4:
        na = a - step[d][0]
        nb = b - step[d][1]

        if map_array[na][nb] == 0:
            a = na
            b = nb
            turn_time = 0
        
        else:
            break

print(count)
"""
