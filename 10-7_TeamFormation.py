def find_parent(parent, x):     #특정 원소가 속한 집합 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): #두 원소가 속한 집합을 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())    #학생수 n(0부터 시작하고, n번까지 있음), 입력으로 주어지는 연산의 개수 m
parent = [0] *(n +1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:       # oper가 0인 경우 두 원소가 속한 집합 합치기
        union_parent(parent, a, b)
    elif oper == 1:     # oper가 1인 경우, 두 원소가 같은 팀에 속해 있는지 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")