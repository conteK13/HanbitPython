#볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
amount = n

ball=[0]*(m+1)
for i in data:
    ball[i] +=1

for i in range(1, m+1):
    amount -= ball[i]
    result += ball[i] * amount

print(result)
