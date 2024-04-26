#연산자 끼워넣기

#입력받기
n = int(input())    #수의 개수
num = list(map(int, input().split()))     #수열
add, sub, mul, div = map(int, input().split())    #+, -, *, /

#초기값 설정
max_result = -1e9
min_result = 1e9 

def dfs(i, temp):
    global max_result, min_result, add, sub, mul, div

    if i == n:      #연산자의 개수가 n -1 개가 되면 값 비교
        max_result = max(max_result, temp)
        min_result = min(min_result, temp)
    
    else:
        if add >0:
            add -= 1
            dfs(i+1, temp+ num[i])
            add +=1
            
        if sub >0:
            sub -=1
            dfs(i+1, temp- num[i])
            sub +=1

        if mul >0:
            mul -=1
            dfs(i+1, temp * num[i])
            mul +=1

        if div>0:
            div -=1
            dfs(i+1, int(temp/ num[i]))
            div +=1


dfs(1, num[0])
print(max_result)
print(min_result)
