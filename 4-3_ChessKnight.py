input_data = input()
row = int(input_data[1]) #행
column = int(ord(input_data[0]))- int(ord('a')) +1 #열 ord함수를 써서 a의 값에 1을 대입해줌

steps = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <= 8:
        result +=1

print(result)

"""
input_data = input()
x = int(input_data[1]) #행
y = int(ord(input_data[0].lower()))- int(ord('a')) +1 #대문자로 받는 경우 처리 방법 .lower()를 사용한다

#dx, dy방식 사용하기
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

result = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        print(nx, ny)
        result +=1

print(result)
"""