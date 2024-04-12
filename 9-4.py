#미래 도시
#n, m = map(int, input().split())    #n도시의 개수, m 간선의 개수
n, m = 4,2

inf = 1e9
graph = [[inf]*(n+1) for _ in range (n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

"""for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
"""
"""graph[1][2] =1
graph[2][1] =1
graph[1][3] =1
graph[3][1] =1
graph[1][4] =1
graph[4][1] =1
graph[2][4] =1
graph[4][2] =1
graph[3][4] =1
graph[4][3] =1
graph[3][5] =1
graph[5][3] =1
graph[4][5] =1
graph[5][4] =1"""

graph[1][3] =1
graph[3][1] =1
graph[2][4] =1
graph[4][2] =1

#x, k = map(int, input().split())    #x 목적지, k 경유지
x, k = 3,4

for z in range(2, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][z]+ graph[z][b])


result = graph[1][k] + graph[k][x]

if result >= inf:
    print("-1")

else:
    print(result)