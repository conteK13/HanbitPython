#외벽 점검
# https://school.programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations      #순열

def solution(n, weak, dist): #n외벽의 총 둘레, weak 취약지점이 담긴 배열, dist 각 친구가 1시간 동안 이동 가능한 거리
    length= len(weak)
    for i in range(length):     #weak를 두배로 만들어 펴는 작업
        weak.append(weak[i]+n)
    
    answer = len(dist) +1 #친구의 수 +1 로 초기화

    for start in range(length): #weak[0]부터 weak[-1] 까지의 지점을 시작점으로 잡기 위해
        for friends in list(permutations(dist, len(dist))): #친구를 나열하는 모든 경우의 수
            count = 1   #투입할 친구의 수
            position = weak[start] + friends[count-1]   #마지막 지점의 위치
            for index in range(start, start + length):  #시작지점으로부터 weak의 모든 개수만큼
                if position < weak[index]:  #weak의 값 도달하지 못할 경우, 친구 한명 추가
                    count +=1
                    if count > len(dist):   #친구의 수가 기준 값을 넘어가게 되면 멈춤
                        break
                    position = weak[index] +friends[count-1]    #다음 취약지점에서 시작하여, 다음 친구의 이동거리만큼 이동
            answer = min(answer, count)

    if answer > len(dist):  #break를 통해 빠져나온 경우
        return -1
    return answer

"""n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]"""

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

result= solution(n, weak, dist)
print(result)