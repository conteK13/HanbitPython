d = [0] * 100

d[1]=1
d[2]=1
n = 99

for i in range(3, n+1):         #3부터 99까지 계산
    d[i]=d[i-1] + d[i-2]

print(d[n])