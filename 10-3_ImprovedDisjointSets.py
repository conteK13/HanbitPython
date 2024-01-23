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

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)      #입력받은 a, b를 union연산

print('각 원소가 속한 집합: ', end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')        #연결된 최상위 부모 값 return

print()

print('부모 테이블: ', end = '')
for i in range(1, v+1):
    print(parent[i], end = ' ')                     #해당 테이블이 속한 부모값 return



