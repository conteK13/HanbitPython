#만들수 없는 금액

n = int(input())
data = list(map(int, input().split()))
data.sort()
target= 1

for i in data:
    if i > target:
        break
    target += i

print(target)
