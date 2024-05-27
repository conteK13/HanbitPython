#정렬된 배열에서 특정 수의 개수 구하기
#조건 : 시간 복잡도 O(log n)

n, x = map(int, input().split())        #n 원소의 개수, x 목표
num = list(map(int, input().split()))   #수열

num.sort()

def first(num, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if (mid == 0 or target > num[mid-1]) and num[mid] == target:    #mid가 0이거나(mid-1을 할 수 없는 경우) mid -1일때 num[mid]가 target인 경우
        return mid
    
    elif num[mid] >= target:
        return first(num, target, start, mid-1)   #end = mid-1로 설정
    
    else:
        return first(num, target, mid+1, end)   #start = mid+1로 설정
    

def last(num, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if (mid == n-1 or num[mid+1] > target and num[mid] == target):
        return mid
    
    elif num[mid] > target: #>= 이 아니라 > 임
        return last(num, target, start, mid-1)   #end = mid-1로 설정
    
    else:
        return last(num, target, mid+1, end)
    
    
def count():
    a= first(num, x, 0, n-1)

    if a== None:
        print(-1)
        return
    
    b= last(num, x, 0, n-1)

    result = b-a +1
    print(result)
    return


count()

