#무지의 먹방 라이브
import heapq        #deque는 선입선출, heapq는 최소값 최대값

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) #q에 (음식, 음식번호) 추가

    sum_value =0 #음식을 먹기 위해 사용한 시간
    previous = 0 #직전 음식을 다 먹기 위해 사용한 시간
    length = len(food_times) #남은 음식 개수

    while sum_value + ((q[0][0] - previous) * length) < k:
        now = heapq.heappop(q)[0]
        sum_value += (now- previous) * length
        length -= 1
        previous = now

    result = sorted(q, key= lambda x:x[1]) #음식 번호를 기준으로 정렬
    return result[(k - sum_value) % length][1]

