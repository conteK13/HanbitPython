#부품 찾기

"""n= int(input())
n_data = list(int(input().split()))
m = int(input())
m_data = list(int(input().split()))
"""

n = 5
n_data = [8, 3, 7, 9, 2]
m = 3
m_data = [5, 7, 9]

def binary_serch(array, target, start, end):
    while start <= end:         #start < end로 하면 xxxxx
        mid = (start + end) //2
        if target == array[mid]:
            return "yes"
        
        elif target < mid:
            end = mid -1
        
        else:
            start = mid+1
    
    return "no"

for i in m_data:
    result = binary_serch(n_data, i, 0, n-1)
    print(result, end = ' ')
    

"""
result =[]
check = False

for i in m_data:
    for j in n_data:
        if i == j:
            result.append('yes')
            n_data.remove(j)
            check = True
            break
    if check == False:
        result.append('no')

for i in result:
    print(i, end = ' ')

"""