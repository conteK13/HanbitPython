#병사 배치하기
n = 7 #int(input())
data = [15, 11, 4, 8, 5, 2, 4] #list(map(int, input().split()))

data.reverse()

dp =[1] * n

for i in range(1, n):
    for j in range(0, i):
        print(i, j)
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))