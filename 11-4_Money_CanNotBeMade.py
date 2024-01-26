n = int(input())
amount = list(map(int, input().split()))
amount.sort()

target = 1

for i in amount:
    if target < i:      #만들수 없는 금액을 찾았을 때 종료
        break
    target += i

print(target)


#해당 문제는 그리디 문제를 많이 풀어봐야 풀수 있을 듯...