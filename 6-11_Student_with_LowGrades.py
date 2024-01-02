n = int(input())

array=[]
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key = lambda student: student[1])
#student를 student[1]을 기준으로 정렬 (점수를 기준으로 정렬한다)

#print(array)
for student in array:
    print(student[0], end = ' ')