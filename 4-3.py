#왕실의 나이트

start = input()
x = int(start[1])
y = ord(start[0]) - ord('a')+1
count =0

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx >= 1 and nx<= 8 and ny >=1 and ny <= 8:
        count +=1

print(count)