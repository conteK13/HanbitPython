n, m = map(int, input().split()) #세로 n, 가로 m

graph = []              #인접행렬(adjacency matrix) 방식으로 노드간 관계를 받음
for i in range(n):
    graph.append(list(map(int, input()))) #여기에 .split()하는 실수 주의!!

print(graph)
def dfs(x, y):          #세로가 x, 가로가 y
    #global 함수를 최대한 사용하지 않는 방향으로 작성함
    if x <= -1 or x >= n or y <=-1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] =1    #방문한 적 있는 곳은 1로 바꿈
        dfs(x+1, y)     #상하좌우로 연결된 곳까지 한번에 확인한다
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

result = 0 #얼음덩어리의 갯수

for i in range(n):
    for j in range(m):

        if dfs(i,j) == True:
            result +=1

print(result)