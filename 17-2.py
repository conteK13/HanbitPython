#정확한 순위
inf = int(1e9)
n, m = 6, 6 #map(int, input().split())
data = [[inf]*(n+1) for _ in range(n+1)]

"""for i in range(n+1):
    data[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1"""

data = [
    [0, inf, inf, inf, inf, inf, inf], 
    [inf, 0, inf, inf, inf, 1, inf], 
    [inf, inf, 0, inf, inf, inf, inf], 
    [inf, inf, inf, 0, 1, inf, inf], 
    [inf, inf, 1, inf, 0, inf, 1], 
    [inf, inf, 1, inf, 1, 0, inf], 
    [inf, inf, inf, inf, inf, inf, 0]
    ]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

result = 0

#여기 비교하는 부분이 좀 어렵다
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if data[i][j] != inf or data[j][i] != inf:
            count +=1
        print(i, j, count, result)

    if count ==n:
        result += 1
        
print(result)