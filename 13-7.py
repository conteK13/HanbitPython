#인구 이동
from collections import deque

#데이터 입력 받기
"""n, l, r =map(int, input().split())  #n 맵크기, 인구차이가 l이상, r 이하
a =[]
for _ in range(n):
    a.append(list(map(int, input().split())))
"""

"""n, l, r = 2, 20 , 50
a = [[50, 30], [20, 40]]"""

n, l, r = 4, 10 , 50
a = [
    [10, 100, 20, 90],
    [80, 100, 60, 70],
    [70, 20, 30, 40],
    [50, 20, 100, 10]
     ]


#인접 이동 경우의 수
move = [(1,0), (0,-1), (-1, 0), (0, 1)]

def solution(a):
    #방문 여부 and 연합 번호 확인용
    visit=[[0] *n for _ in range(n)] 

    q = deque()
    count = 1   #연합의 개수
    check = False

    for i in range(n):
        for j in range(n):
            if visit[i][j]== 0:      #방문한적 없다면
                q.append((i,j))     #q에 현재 위치 추가
                visit[i][j] = count #현재 위치 union
                sum_population = 0
                sum_count=0
                unite = []
                while q:
                    x, y = q.popleft()
                    
                    unite.append((x, y))
                    sum_population += a[x][y]
                    sum_count +=1

                    for dx, dy in move:
                        nx = x + dx
                        ny = y + dy
                        
                        if nx >=0 and nx < n and ny >=0 and ny <n:  #nx, ny가 범위를 벗어나지 않는 경우
                            if visit[nx][ny]==0:
                                temp = abs(a[x][y] - a[nx][ny])
                                if temp >= l and temp <= r:     #인구차가 범위의 내에 있는 경우
                                    check = True
                                    q.append((nx, ny))          #q에 nx, ny추가
                                    visit[nx][ny] = count #현재 위치 union
                for x, y in unite:
                    a[x][y] = sum_population //sum_count

                
                count +=1   #count를 +1하여 방문하지 않은 노드로 이동

    return check

result = 0
while True:
    if solution(a):
        print(a)
        result+=1
    else:
        break

print(result)