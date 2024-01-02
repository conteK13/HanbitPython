#원소의 개수 n을 입력받지 않고 len(array)로 처리하는 코드

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 #소수점 아래는 버리고 정수로 설정. start값이 mid 값이 될 수 있음

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)
    
target = int(input())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, len(array)-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
    

"""
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 #소수점 아래는 버리고 정수로 설정. start값이 mid 값이 될 수 있음

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)
    
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
"""