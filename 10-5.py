#크루스칼 알고리즘 소스

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
parent = [0] *(v+1)

edges =[]
result = 0

for i in range(e):
    a, b, cost= map(int, input().split())
    edges.append((cost, a, b))  #cost를 기준으로 오름차순 정렬하기 위해서

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):    #a,b가 사이클이 발생하지 않으면
        union_parent(parent, a, b)
        result += cost

print(result)
