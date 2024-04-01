#게임 개발

n, m = map(int, input().split())
a, b, d = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))
visit= [[0]*m for _ in range(n)]

direct = [(-1,0), (0,1), (1,0), (0,-1)]
visit[a][b] = 1
count = 1

turn = 0
while True:
    d +=1               #왼쪽방향으로 시선 돌리기
    if d > 3:  d -=3

    na = a + direct[d][0]
    nb = b + direct[d][1]

    turn += 1 

    if data[na][nb] != 1 and visit[na][nb] == 0:
        a, b = na, nb
        visit[a][b] = 1
        turn = 0
        count += 1
    
    if turn >= 4:
        a -= direct[d][0]
        b -= direct[d][1]
        turn = 0

        if data[a][b] == 1:
            break

print(count)