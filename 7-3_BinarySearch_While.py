#원소의 개수 n을 입력받지 않고 len(array)로 처리하는 코드

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid+1
    
    return None

target = int(input())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, len(array)-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)

"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid+1
    
    return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
"""