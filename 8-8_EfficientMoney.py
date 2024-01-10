n, m = map(int, input().split())    #화폐갯수는 n, 원하는 값 m

array = []
for i in range(n):                  #화폐입력 받기
    array.append(int(input()))

d = [10001] * (m+1)                 #불가능한 값 입력
d[0] = 0                            #d[0] = 0

for i in range(n):                  
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:    #(i-k)원을 만드는 방법이 있는 경우
            d[j] = min(d[j], d[j- array[i]]+1)
            #print(d)

if d[m] == 10001:
    print(-1)

else:
    print(d[m])