#고정점 찾기
#시간 복잡도 O(log n)

n = int(input())
num = list(map(int, input().split()))

num.sort()

def search(num, start, end):
    mid = (start + end) //2

    if start > end:
        print(-1)
        return

    if num[mid] == mid:
        print(mid)
        return
    
    elif num[mid] > mid:
        return search(num, start, mid-1)
    
    else:
        return search(num, mid+1, end)

    
search(num, 0, n-1)