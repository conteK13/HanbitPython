n = int(input())
count = 0

for h in range(n+1): #시,  range는 0부터 n-1까지이므로 1 보상
    for m in range(60): #분
        for s in range(60): #초
            if '3' in str(h) + str(m) + str(s):
                count +=1

print(count)

"""
#00시 00분 00초부터 n시 59분 59초 사이의 숫자 x가 하나라도 포함된 경우의 수 계산

n = int(input())
x = input()
count = 0

for h in range(n+1): #시,  range는 0부터 n-1까지이므로 1 보상
    for m in range(60): #분
        for s in range(60): #초
            if x in str(h) + str(m) + str(s):
                count +=1

print(count)
"""