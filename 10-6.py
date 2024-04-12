#위상 정렬 소스코드
#선후 구조

from collections import deque

v, e = map(int, input().split())#노드, 간선 개수
indegree = [0] * (v+1)      #진입차수(연결된 input간선의 수 )
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)      #a에 연결된 b 저장
    indegree[b] +=1          #b에 진입 차수 +1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:    #진입차수가 0인 경우만 q에 삽입
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -=1     #연결된 노드의 진입차수 -1
            if indegree[i] ==0: #진입차수가 0이면 q에 삽입
                q.append(i)


    for i in result:
        print(i, end = ' ')

topology_sort()