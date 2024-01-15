import sys
input = sys.stdin.readline      #input이 sys.stdin.readline의 속도를 갖게 됨.
inf = int(1e9)                  #inf에 무한대값(1,000,000,000) 입력, 혹은 987654321을 입력하기도 함

n, m = map(int, input().split())        #노드의 수와 간선의 개수 입력
start = int(input())                    #시작 노드 입력 받기
graph = [[] for i in range(n+1)]        #노드간 연결관계를 나타내는 리스트. 인접리스트(Adjacency List) 방식으로 생성
visited = [False] * (n+1)               #방문여부를 확인하는 리스트. False로 초기값 설정
distance = [inf] *(n+1)                 #노드간 거리를 작성하는 리스트. inf 값으로 초기값 설정.


for _ in range(m):                      #간선의 개수만큼 관계를 입력받음.
    a, b, c = map(int, input().split()) #a는 시작 노드, b는 도착 노드, c는 그 사이 간선의 값
    graph[a].append((b,c))


def get_smallest_node():                
    min_value = inf
    index = 0                       #최단 거리가 가장 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:  #노드간 거리가 min_value보다 낮고, 방문한 적이 없을 경우
            min_value = distance[i]                     #min_value는 distance[i]값으로 변경
            index = i
    return index

def dijkstra(start):
    distance[start] = 0             #시작값의 거리는 항상 0, 그리고 방문여부는 True로 설정
    visited[start] = True
    for j in graph[start]:          #시작점과 연결된 노드 값으로 반복
        distance[j[0]] = j[1]       #distance[graph[start][i][0]], graph[start][i][0] = 시작 노드와 연결된 노드, graph[start][i][0] = 연결된 간선의 값

    for i in range(n-1):
        now = get_smallest_node()   #시작점과 가장 가까운 노드
        visited[now] = True
        for j in graph[now]:        
            cost = distance[now] + j[1]     #cost = distance[now]+ graph[now][j][1]
            if cost < distance[j[0]]:       #현재 노드를 거쳐서 다른 노드로 이동하는게 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start)


#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == inf:
        print("INFINITY")
    else:
        print(distance[i])
