n = int(input())

#n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
    print(i, end = ' ')