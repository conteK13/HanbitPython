import heapq
import sys

#n도시의 개수, m 통로의 개수, c 도시
input = sys.stdin.readline  #입력받는 시간을 줄이기 위해
inf = 1e9

n, m, c = map(int, input().split()) 
graph = [[] for _ in range(n+1)]
distance = [inf] *(n+1)


for _ in range(m):
    x, y, z = map(int, input().split()) #x 시작점, y 도착점, z 보내는 데 걸리는 시간
    graph[x].append((y, z))

def main(start):
    q=[]
    heapq.heappush(q, (start, 0))   #초기값
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)    #now 지금 위치, dist 걸리는 시간
        if distance[now] < dist:        #기본값은 inf이므로, dist보다 작다는 건, 이미 처리한 적 있다는 뜻
            continue

        for i in graph[now]:            #now와 연결된 도시와 거리를 하나씩 받아서 처리
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

main(c)
count = 0
max_dist =0

for d in distance:
    if d != inf:
        count += 1
        max_dist = max(max_dist, d)

print( count -1, max_dist)

