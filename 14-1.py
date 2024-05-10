#국영수

n = int(input())
data = []
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append([name, int(kor), int(eng), int(math)])

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
"""
-x[1] kor를 기준으로 내림차순
x[2] eng를 기준으로 오름차순
-x[3] math를 기준으로 내림차순
x[0] name을 기준으로 오름차순
"""

for student in data:
    print(student[0])