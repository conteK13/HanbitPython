from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # start =1, queue = deque([1])
    visited[start] = True #방문처리

    while queue:
        v= queue.popleft()  #가장 왼쪽의 원소 출력
        #print(v, end = ' ')
        print("방문한 노드 :",v, " / ", v, "노드와 연결된 노드 :", graph[v])
        #현재 노드와 연결된 노드들 확인

        for i in graph[v]:  # v 노드에 연결된 노드들로 루프를 돌리겟음
            if not visited[i]:  #노드 i에 방문한 적이 없다면
                print("새로 방문한 노드 :", i)                          #방문한적 없는 노드를 찾은 경우
                queue.append(i) #queue에 새로운 노드 i 추가
                visited[i] = True
        
        print("현재 노드", v, "에선 더이상 갈곳이없으므로, 다음 queue값으로 이동하겠음\n")

    print("모든 queue를 확인하였으므로 함수 종료")
"""

def bfs(graph, start, visited):
    queue = deque([start]) # start =1, queue = deque([1])
    visited[start] = True #방문처리

    while queue:
        v= queue.popleft()  #가장 왼쪽의 원소 출력
        print(v, end = ' ')

        for i in graph[v]:  # v 노드에 연결된 노드들로 루프를 돌리겟음
            if not visited[i]:  #노드 i에 방문한 적이 없다면
                queue.append(i) #queue에 새로운 노드 i 추가
                visited[i] = True
"""

#노드간 연결 정보를 인접리스트(Adjacency List)로 표현
graph = [
    [],         #노드 0과 연결된 노드 없음
    [2, 3, 8],  #노드 1과 연결된 노드 작성
    [1, 7], 
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1,7]
]

visited = [False] * 9   #노드 0부터 노드 9까지 방문 여부를 확인할 리스트

bfs(graph, 1, visited)