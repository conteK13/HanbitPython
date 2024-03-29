#큰 수의 법칙(LLN : Law of Large Number)

#배열의 크기 N
#주어진 수를 M번 더함
#같은 인덱스는 연속해서 K번만 더할수 있음

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
""" TEST를 위해 입력받는 시간을 단축
n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
"""

data.sort()
first = data[-1]
second = data[-2]


result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -=1

print(result)

"""
#result = first * k * (m//(k+1)) + second *(m//(k+1)+ m%(k+1))
count = k * (m//(k+1))
result = first * count
result += second * (m - count)

print(result)
"""