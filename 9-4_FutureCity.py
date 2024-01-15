#Floyed_Warshall 방식으로 풀이

inf = int(1e9)

n, m = map(int, input().split())    #전체 회사의 수 N, 경로의 수 M
graph = [[inf]*(n+1) for i in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    #양방향 이동 가능, 이동까지 거리는 모두 동일하게 1 이므로 이렇게 설정 가능함.

x, k = map(int, input().split())

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= inf:
    print("-1")
else:
    print(distance)
