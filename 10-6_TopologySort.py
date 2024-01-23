from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)              #진입 차수 0으로 초기화
graph = [[] for _ in range (v+1)]   #각 노드와 연결된 간선 정보 연결

for _ in range(e):      #방향 그래프의 모든 간선 정보 입력
    a, b = map(int, input().split())
    graph[a].append(b)  #a에서 b로 이동 가능
    indegree[b] += 1    #b에 진입 차수 +1

def topology_sort():
    result = []
    q = deque() #que기능을 위한 deque 라이브러리 사용

    for i in range(1, v+1):
        if indegree[i] == 0:    #진입차수가 0인 노드를 큐에 삽입
            q.append(i)
    
    while q:                        #que가 전부 빌 때까지
        now = q.popleft()           #que에서 원소 꺼내기
        result.append(now)          #result에 now(que에 꺼낸 원소)
        
        for i in graph[now]:        #현재 노드와 연결된 노드
            indegree[i] -=1         #진입 차수 -1씩 빼기

            if indegree[i] == 0:    #진입차수가 0이 되면 que에 삽입
                q.append(i)

    for i in result:
        print(i, end = ' ')

topology_sort()