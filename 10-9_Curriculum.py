from collections import deque
import copy

n = int(input())            #동빈이가 들으려 하는 강의의 수
indegree = [0] * (n+1)      #진입차수. 0으로 초기화
graph = [[] for _ in range (n+1)]   #각 노드와 연결된 간선 연결 정보
time = [0] * (n+1)          #각 강의 시간

for i in range(1, n+1):        #모든 간선 정보 입력받기
    data = list(map(int, input().split()))
    time[i] = data[0]       #입력받은 data중에서 첫 번째(data[0])는 시간정보를 담고 있음

    #선행되어야 하는 강의 정보 받기
    for x in data[1:-1]:    #2번째 부터 뒤에서 두번째 값까지. #range함수는 그 수 전의 수까지 출력하므로
        indegree[i] += 1    #해당 강의의 진입 차수 1씩 증가
        graph[x].append(i)  #graph에 간선 정보 추가

def topology_sort():
    result = copy.deepcopy(time)    #리스트 값 복사. 대입 연산하면 값이 변경될때 문제가 생길수 있음
    q = deque() #que기능 사용

    #처음 시작할 때, 진입차수가 0인 강의를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] ==0:
            q.append(i)

    while q:
        now = q.popleft()   #que에서 원소 꺼내기

        for i in graph[now]: #인접한 강의 확인
            result[i] = max(result[i], result[now] + time[i])   #더 오랜 시간이 걸리는 경우로 저장
            indegree[i] -= 1
            if indegree[i] == 0:    #새롭게 진입차수가 0이 된 강의 que에 삽입
                q.append(i)

    
    for i in range(1, n+1):
        print(result[i])

topology_sort()