#금광

tc = int(input())    #test case의 개수

for _ in range(tc):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    data=[]     #일렬로 입력받은 데이터를 n*m 형태의 리스트로 변환


    for i in range(n):
        data.append(array[i*m :(i+1)*m])

    result = [[0]* (m+2) for _ in range(n+2)]   #상하좌우에 0을 추가한 맵
    
    for i in range(n):
        result[1+i][1] = data[i][0] #result의 1열(0열은 0)에 data의 0열을 넣는다


    for j in range(1, m):  #열
        for i in range(n):  #행
            result[i+1][j+1] = data[i][j]+max(result[i][j], result[i+1][j], result[i+2][j])
    answer = 0
    
    for i in range(1, n+1):
        answer = max(answer, result[i][m])

    print(answer)