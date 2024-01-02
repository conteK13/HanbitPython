array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i           #i번째 자리의 수와 비교함
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j   #더 작은 수가 min_index가 됨
    
    array[i], array[min_index] = array[min_index], array[i]     #파이썬 스와이프. (주의)다른 언어와 다름


print(array)