inf = int(1e9)  #inf에 무한대값(1,000,000,000) 입력, 혹은 987654321을 입력하기도 함

n = int(input())    #모든 노드의 개수
m = int(input())    #모든 간선의 개수

graph = [[inf]*(n+1) for i in range(n+1)]   #graph를 n*n 크기의 리스트로 만듦. 초기값은 inf 로 설정

for a in range(1, n+1):     #자기 자신과의 거리는 0으로 변경
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0


for _ in range(m):          #간선정보 입력받음
    a, b, c = map(int, input().split())     #a에서 b로 가는 값이 c
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])    #a에서 b로 바로 가는 것과, k를 거쳐간 것 중에 더 짧은 것을 선택


#print(graph)를 하면, 0번째 원소가 출력되므로, 해당 부분을 제외하고 출력하기 위해 range를 1부터 시작하도록 설정
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == inf:
            print("INFINITY", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()