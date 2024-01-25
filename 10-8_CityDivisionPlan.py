def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e  = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0
result_edges = []

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        result_edges.append((cost, a, b)) #크루스칼 알고리즘을 통해 최소 신장 트리를 구성
        last = cost     #for문을 도는 동안, 마지막 last값이 가장 cost가 높은 값이 됨

print(result - last)    #최소신장트리에서 가장 비용이 큰 간선 제거
print(result_edges)     

#cost값이 가장 큰 last를 뺏을 때, 어떻게 구성되는 지 구분 하는 방법