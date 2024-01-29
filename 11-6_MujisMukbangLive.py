#Gredy 방식으로 풀이

import heapq            #우선순위 que를 사용하기 위해 import

def solution(food_times, k):
    if sum(food_times) <= k:    #섭취해야 할 음식이 없는 경우
        return -1
    
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) #que에 (음식시간, 음식번호) 순으로 입력. 음식 번호는 1부터 시작하기 위해 +1
    
    sum_value = 0   #먹기 위해 사용한 시간
    previous = 0    #직전에 다 먹은 음식 시간
    length = len(food_times)    #남은 음식의 개수

    while sum_value + ((q[0][0] - previous)* length) <= k: #sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 남은 음식의 개수와 k비교
        now = heapq.heappop(q)[0]   #남은 음식중 가장 음식 시간이 짧은 경우
        sum_value += (now - previous) * length 
        length -= 1         #남은 음식의 개수 -1
        previous = now      #이전 음식 시간 재설정

    answer = sorted(q, key=lambda x: x[1])  #음식의 번호를 기준으로 정렬
    return answer[(k - sum_value) % length][1]  #(k - 먹기 위해 사용한 시간) = 남은 시간, 남은 음식의 개수로 나눈 나머지(현재 위치)의 음식 번호 return



#정확성 및 효율성에서 Fail
"""
def solution(food_times, k):
    offset = 0
    
    #if sum(food_times) <= k:       #섭취할 음식이 없다면, 이라는 조건문 추가 안했었음.
    #    return -1

    for i in range(k+1):
        now = (i+ offset) % len(food_times) 

        if food_times[now] == 0:
            offset +=1
            now = (i+ offset) % len(food_times) 

        food_times[now] -= 1
    answer = now +1
    return answer

#food_times = map(int, input().split())
#k = int(input())

food_times = [3, 1, 2, 4, 1]
k = 7

result = solution(food_times, k)
print(result)
"""