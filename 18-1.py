#여행 계획
#여행 계획의 모든 도시들이 한 union에 있다면 True

def find_parent(parent, x): #부모 값 반환
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b): #두개의 union 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:   #둘중의 더 작은 값으로 부모값 변환
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())    #n 여행지의 수, m 도시의 수

parent= [0] * (n+1)     
for i in range(n+1):    #부모값을 본인으로 변경
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:    #연결 되어 있다면, 두 도사의 부모값을 합치기
            union_parent(parent, i+1, j+1)


plan = list(map(int, input().split()))   #여행 목적지

result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")

