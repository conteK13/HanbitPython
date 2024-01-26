def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])       #경로 압축기법(Path Compression)
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:       #부모 값을 더 작은 값으로 변경
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)    #parent를 0으로 초기화
for i in range(1, v+1):
    parent[i] = i       #모든 원소가 자기 자신을 부모로 가짐

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):    #사이클이 발생한 경우 종료
        cycle = True
        break
    else:       #사이클이 발생하지 안은 경우 union연산 진행
        union_parent(parent, a, b)


if cycle:
    print("사이클이 발생했습니다.")

else:
    print("사이클이 발생하지 않았습니다.")