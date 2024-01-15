#Dijkstra 방식으로 풀이

import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n, m, start = map(int, input().split())
graph = [[]*(n+1) for i in range(n+1)]
distance = [inf] *(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)


count = 0           #도시 c에서 보낸 메시지를 받은 도시의 개수
max_distance = 0    #도시들이 모두 메시지를 받는 데 걸리는 시간(최대 전달 시간)
                    #max_distance = max(distance)와의 차이가 뭘까.
for d in distance:
    if d != inf:
        count+=1
        max_distance= max(max_distance, d)
    
print(count-1, max_distance)