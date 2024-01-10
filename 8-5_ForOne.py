x = int(input())

d = [0] * (x+1)

for i in range(2, x+1):
    #현재의 수에서 1을 빼는 경우
    d[i] = d[i -1] +1
    print("현재의 수 :", i, d)

    #현재의 수가 2로 나누어 지는 경우
    if i % 2==0:
        d[i] = min(d[i], d[i//2]+1)
        print("2로 나눈 경우", d)

    #현재의 수가 3로 나누어 지는 경우
    if i % 3 ==0:
        d[i] = min(d[i], d[i//3]+1)
        print("3로 나눈 경우", d)
    
    #현재의 수가 5로 나누어 지는 경우
    if i % 5 ==0:
        d[i] = min(d[i], d[i//5]+1)
        print("5로 나눈 경우", d)


print(d[x])