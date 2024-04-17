def rotation(key):
    a = len(key)        #행의 수
    b = len(key[0])     #열의 수

    result = [[0]*a for _ in range(b)]

    for x in range(b):
        for y in range(a):
            result[x][a-y-1] = key[y][x]
    
    return result


def check(extend_lock):
    n = len(extend_lock)//3

    for x in range(n, n*2):
        for y in range(n, n*2):
            if extend_lock[x][y] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    #lock의 크기를 3배로 늘리기
    extend_lock = [[0]*(n*3) for _ in range(n*3)]
    for x in range(n):
        for y in range(n):
            extend_lock[x+n][y+n] = lock[x][y]
    
    #lock에 key대입
    for _ in range(4):
        key = rotation(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        extend_lock[x+i][y+j] += key[i][j]
                
                if check(extend_lock):
                    return "true"
                
                for i in range(m):
                    for j in range(m):
                        extend_lock[x+i][y+j] -= key[i][j]
    
    return "false"

key = [[0, 0, 0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
result = solution(key, lock)
print(result)