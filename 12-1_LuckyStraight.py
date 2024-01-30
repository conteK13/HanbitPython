n = input()     #정수로 입력된 숫자를 str로 받음
length = len(n)//2  #n의 길이를 1/2하여, 왼쪽과 오른쪽의 길이를 받는다.
                    #len(n)/2로 계산하면, float형으로 출력하며 error 발생할 수 있음

sum= 0
for a in n[:length]:
    sum += int(a)

for b in n[length:]:
    sum -= int(b)

if sum == 0:
    print("LUCKY")
else:
    print("READY")



""" #변수를 sum1, sum2로 두개를 쓰는 경우
sum1 = 0
sum2 = 0

for a in n[:length]:
    sum1 += int(a)

for b in n[length:]:
    sum2 += int(b)

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
"""