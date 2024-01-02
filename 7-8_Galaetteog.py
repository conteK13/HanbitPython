n, m = map(int, input().split()) #n은 떡의 개수, m은 고객이 원하는 떡의 길이
array = list(map(int, input().split())) #떡의 길이 입력

start = 0
end = max(array)    #떡의 최대 길이를 end로 설정
result = 0          #적절한 높이의 최대값 설정

while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:             #떡의 길이가 자르는 곳(mid)보다 작다면, 떡의 길이 무시.
            total += x -mid     #mid를 기준으로 자르고, 남은 길이 합산.
    
    if total < m:               #떡의 길이가 부족하므로 더 자르기 위해 end 재설정
        end = mid - 1
    else:                       #떡의 길이가 충분하므로 덜 자르기 위해 start 재설정, 그리고 result 갱신
        result = mid
        start  = mid +1

print(result)