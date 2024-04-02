#떡볶이 떡 만들기

"""n, m = map(int, input().split())
data = list(int(input().split()))"""
n,m = 4,5
data = [19, 15, 10, 17]


start = 0
end = max(data)

while start<=end:
    mid = (start+end)//2
    total = 0

    for i in data:
        if i>mid:
            total += i-mid

    if total == m:
        result = mid

    elif total > m:    #더 많이 자름
        result = mid
        start = mid+1

    else:               #덜 자름
        end = mid-1
    
    #print(start, end, mid)


print(result)

"""
def solution():
    for i in range(max(data)-1 , 1, -1):
        result = 0
        for j in data:
            if j - i >0:
                result += j-i

                if result >= m:
                    return i
                
print(solution())
"""