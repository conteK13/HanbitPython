#정수 삼각형

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = [[0]*(n+1) for _ in range(n+1)]
result[1][1] = data[0][0]

for i in range(1, n):
    for j in range(i+1):
        result[i+1][j+1] = data[i][j] + max(result[i][j+1], result[i][j])


answer = 0
for i in range(n):
    answer = max(answer, result[n][i+1])

print(answer)
