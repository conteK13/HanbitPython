#숫자 카드 게임
"""
#1 입력받는 동시에 min중의 max값을 탐색
n, m = map(int, input().split())
data = []
result = 0

for _ in range(n):
    data=(list(map(int, input().split())))
    min_value = min(data)
    result = max(result, min_value)
"""

"""
n, m = 3, 3
data = [
    [3, 1, 2],
    [4, 1, 4],
    [2, 2, 2]
]
"""
n, m = 2, 4
data = [
    [7, 3, 1, 8],
    [3, 3, 3, 4]
]

#입력을 모두 받은 상태에서 계산
result = min(data[0])

for i in range(1, n):
    result = max(result, min(data[i]))

print(result)