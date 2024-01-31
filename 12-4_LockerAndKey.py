def right_rotate_matrix_by_90_dgree(a):   #list를 입력받아서 오른쪽으로 90도 회전시키는 함수
    n = len(a)     #입력받은 리스트의 행의 길이   #이 조건에서 N*N이므로 열의 길이도 동일하다.
    m = len(a[0])  #입력받은 리스트이 열의 길이
    result = [[0] * m for _ in range(n)]    #행과 열을 swap하여 새로운 리스트 result 생성

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]      
            
            #result      a          #EX) result[1][2] = a[0][1]
            #7 4 1       1 2 3      #EX) result[0][1] = a[1][0]
            #9 5 2       4 5 6
            #9 6 3       7 8 9
            
    return result

def left_rotate_matrix_by_90_dgree(a):  #list를 입력받아서 왼쪽으로 90도 회전시키는 함수
    n = len(a)
    m = len(a[0])
    result = [[0] * m for _ in range(n)] 

    for i in range(n):
        for j in range(m):
            result[n-j-1][i] = a[i][j]

            #result      a          #EX) result[1][0] = a[0][1]
            #3 6 9       1 2 3      #EX) result[2][1] = a[1][0]
            #2 5 8       4 5 6
            #1 4 7       7 8 9

def check(new_lock):    #새로운 lock(3배 늘린 리스트)가 열렸는지 확인하는 함수
    lock_length = len(new_lock)//3        #lock을 3배 늘렸기 때문에 //3 해줘야 한다.
                                #이때 /3을 하면 float형태로 반환되므로 TypeError 발생
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
               return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4): #0도, 90도, 180도, 270도 4번 수행함
        key = right_rotate_matrix_by_90_dgree(key)  #key를 오른쪽으로 90도 회전

        for x in range(n*2):        #new_lock이 n*3이므로 n*2만큼 보정
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                
                for i in range(m):      #check함수를 사용해서 False라면 더한 값을 그대로 빼서 복원
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
    
key = [[0, 0, 0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
result = solution(key, lock)
print(result)