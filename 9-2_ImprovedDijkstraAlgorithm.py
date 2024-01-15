import heapq                    #동작 시간을 줄이기 위해 Heap구조 사용
import sys
input = sys.stdin.readline      #input이 sys.stdin.readline의 속도를 갖게 됨.
inf = int(1e9)                  #inf에 무한대값(1,000,000,000) 입력, 혹은 987654321을 입력하기도 함


n, m = map(int, input().split())    #노드의 수와 간선의 개수 입력
start = int(input())                #시작 노드 입력 받기
graph = [[] for i in range(n+1)]    #노드간 연결관계를 나타내는 리스트. 인접리스트(Adjacency List) 방식으로 생성
distance = [inf] * (n+1)            #노드간 거리를 작성하는 리스트. inf 값으로 초기값 설정.



for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkastra(start):
    q = []
    heapq.heappush(q, (0, start))   #시작 점으로 가기 위한 최단 경로를 0으로 설정하여 q에 삽입
    distance[start] = 0

    while q:                        #q가 비어있지 않다면
        dist, now = heapq.heappop(q)    #now는 가장 가까운 최단 노드, dist는 현재 노드와의 거리
        if distance[now] < dist:
            #이미 처리한 적 있다면 무시
            #9-1과 달리 visit은 사용하지 않았던 이유가 여기서 처리할 예정이었기 때문임
            continue

        for i in graph[now]:        #현재 노드와 다른 인접한 노드 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:   #현재 노드에서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))     #q에 새로운 값 추가
                #print(q)
                #print(distance)  

        #print("while문 한턴 종료")

dijkastra(start)

for i in range(1, n+1):
    if distance[i]== inf:
        print("INFINITY")
    else:
        print(distance[i])