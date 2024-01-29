#직접 작성한 코드보다 시간이 더 짧을 듯
n, k = map(int, input().split())
ball = list(map(int, input().split()))

array = [0] * 11    #볼링공의 무게별 리스트 작성(볼링공의 무게는 최대 10이므로 10+1로 설정)

for x in ball:
    array[x] += 1   #해당하는 무게에 볼링공 

result = 0

for i in range(1, k+1):
    n -= array[i]       #무게가 i인 볼링공을 경우의 수에서 제거
    result += array[i] * n  #result에 무게가 i인 경우와 i가 아닌 경우의 곱을 더한다.

print(result)


"""
#직접 작성한 코드, 구현은 쉽지만 실제 동작시간은 책의 코드가 더 적절할 듯.

n, k = map(int, input().split())            #볼링공의 개수 n, 공의 최대 무게 k
ball = list(map(int, input().split()))      #각 볼링공의 무게 ball

count = 0                               #조건을 만족할때 마다 count를 1씩 증가 시킴
for a in range(n-1): #0 1 2 3           #두 사람의 볼링공의 조합을 보는 것이기 때문에 range범위를 이렇게 설정
    for b in range(a+1, n): #1 2 3 4
        if ball[a] != ball[b]:          #볼링공의 무게가 서로 다를 경우
            count += 1

result = count
print(result)
"""