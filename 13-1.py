#특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split())  #n 도시의 개수, m 도로의 개수, k거리 정보, x 출발 도시
inf = 1e9
graph= [[] for _ in range(n+1)]

for _ in range(m):      #a에서 b로 가는 거리 = 1
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0     #출발 지점의 거리는 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:   #한번도 방문한 적 없는 경우
            distance[next_node] = distance[now] +1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)