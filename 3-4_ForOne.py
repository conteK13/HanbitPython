#n, k = map(int, input().split())
n = 17
k = 5
count = 0
'''
while n>= k:
    if n % k == 0 :
        n = n/k
        count +=1
    else:
        n -=1
        count +=1

while n != 1:
    n -=1
    count +=1
'''

while True:
    target = (n//k) * k
    count += n-target
    print("n:", n, " target:", target, " count:", count)
    n= target #뺄셈 완료한 후의 값으로 업데이트 (i++, ++i의 차이같은 거임)
    print("n:", n, " target:", target, " count:", count)
    if n < k:
        break

    count +=1
    n = n//k
    print("n:", n, " target:", target, " count:", count)

count += (n-1) #while문에서 나머지를 0으로 만들었으므로 그 값을 보정
print(count)