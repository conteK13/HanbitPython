#안테나

n = int(input())
data = list(map(int, input().split()))
data.sort()     #sort()의 ()잊지 말것

result = data[(n-1)//2]         #정렬한 data의 중간값이 최적의 결과임

print(result)