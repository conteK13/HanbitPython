'''
n=5 #배열의 크기
m=8 #숫자가 더해지는 횟수
k=3 #최대 연속 횟수
num = [2, 4, 5, 4, 6]

num.sort()
first = num[-1] #소괄호'()' 로 착각하지 않도록 주의
second = num[-2] 

q = m // (k+1) #int(m/(k+1))과 m//(k+1)의 차이가 무엇일까 #Quotient
r = m % (k+1) #Reminder

result = (first * k + second) * q + first * r
'''
n, m, k = map(int, input().split())
num  = list(map(int, input().split()))

num.sort()
first = num[n-1] #소괄호'()' 로 착각하지 않도록 주의
second = num[n-2] 

count = (m // (k+1)) * k
count += m % (k+1)

result = first * count
result += second * (m-count)

#변수의 개수를 줄이고, 계산을 간단하게 수정함
print(result)