import time         #시간 측정을 위해
n = int(input())    #모험가의 수
x = list(map(int, input().split()))     #모험가의 공포도

start_time = time.time()
x.sort()    #모험가의 공포도 순으로 정렬

result = 0  #모험가 그룹의 최대수
count = 0 #현재 그룹에 포함된 인원 수

for i in x:             #공포도 순으로 for문 돌리기
    count += 1          #인원수 +1
    if i <= count:      #공포도가 인원수보다 작다면
        result += 1     #모험가 그룹 +1
        count = 0       #인원수 초기화

print(result)
end_time = time.time()
print("time : ", end_time-start_time)

