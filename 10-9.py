#커리큘럼
from collections import deque
import copy

n = int(input())

indegree = [0] *(n+1)
graph = [[] for _ in range(n+1)]
time = [0] *(n+1)   #각 강의 시간

for i in range(1, n+1):     #i는 강의 번호
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:    #선교육 강의
        indegree[i] += 1    #들어야 하는 강의 갯수 만큼 진입차수 증가
        graph[x].append(i)  #선교육 강의에 현재 강의 번호 추가

def topology_sort():
    result = copy.deepcopy(time)    #단순 대입 연산을 하면 값이 변경될때 문제가 발생할 수 있으므로
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:    #진입차수가 0인 시험을 먼저 q에 입력
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i]) 
            indegree[i] -= 1    #해당 노드와 연결된 노드의 진입 차수 -1
            if indegree[i] ==0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()