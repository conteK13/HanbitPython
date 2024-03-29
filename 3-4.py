#1이 될 때 까지

#n, k = map(int, input().split())
n, k = 17, 4
count = 0
"""
#1 단순 계산(n의 값이 커지면 이것보다 더 단순화 하여 풀어야 한다.)
while True:
    if n == 1:
        break

    if n%k ==0:
        n=n//k
    else:
        n -=1

    count +=1
"""
#2 -1씩 빼는 시간을 줄이기 위해, k의 배수까지 한번에 빼기
while True:
    target = (n//k) *k
    count += n- target

    n = target

    if n< k:    #n이 k보다 작을때(나눌수 없을 때) loop 탈출
        break
    n = n//k
    count +=1

count += (n-1)
print(count)