#퇴사

n = int(input())    #퇴사 날
data = []
result = [0] * (n+1)
max_value = 0

for i in range(1,n+1):
    t, p = map(int, input().split())
    data.append((i,t,p))

data.reverse()

for index, t, p in data:
    if index + t <= n:
        result[index] = max(result[index+t] + p, max_value)
        max_value = result[index]
    else:
        result[index] = max_value

print(max_value)