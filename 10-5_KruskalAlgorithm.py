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

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0
result_edges = []       #연결된 노드를 확인하기 위해

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  #비용순으로 정렬하기 위해 cost를 가장 앞으로 설정

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):    #사이클이 발새하지 않는 경우에만 집합에 포함 
        union_parent(parent, a, b)
        result_edges.append((cost, a, b))
        result += cost

print(result)
print(result_edges)