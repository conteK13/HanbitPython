#감시 피하기

n = int(input())    #복도의 크기
data =[]
s, t, w  =[], [], []

for i in range(n):
    data.append(list(input().split()))

    for j in range(n):
        if data[i][j] == 'S':
            s.append((i,j))
        elif data[i][j] == 'T':
            t.append((i,j))

def check(s, t, w):
    temp = False
    for sx, sy in s:
        for tx, ty in t:
            if sx == tx:    #학생과 선생이 동일한 행에 있는 경우
                for wx, wy in w:
                    if wx == tx and min(sy, ty) < wy and max(sy, ty) > wy:
                        temp = True
                
                if temp == False:
                    return False
                
                temp = False
            
            if sy == ty:
                for wx, wy in w:
                    if wy == ty and min(sx, tx) < wx and max(sx, tx) > wx:
                        temp = True

                if temp == False:
                    return False
                
                temp = False
    
    return True
result = False

def solution(count):
    global result
    if count == 3:
        if check(s, t, w):
            result = True
            return 
        
        return

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = "W"
                w.append((i, j))
                count +=1
                solution(count)
                data[i][j] = "X"
                w.remove((i, j))
                count -=1

solution(0)
if result:
    print("YES")
else:
    print("NO")