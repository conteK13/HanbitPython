#위에서 아래로

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))


data = sorted(data, reverse=True)

for i in data:
    print(i, end = ' ')

