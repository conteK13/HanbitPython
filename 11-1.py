#모험가 길드

n = int(input())

data=list(map(int, input().split()))
print(data)
data.sort()

result =0
group_count = 0

for i in data:
    group_count +=1
    if i <= group_count:
        result +=1
        group_count = 0

print(result)
