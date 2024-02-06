from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):     #길이를 2배로 늘이기
        weak.append(weak[i] + n)
    answer = len(dist) + 1 #투입할 친구의 최소값을 찾기 위해 초기화

    for start in range(length): #시작점을 0부터 length -1로 설정 
        for friends in list(permutations(dist, len(dist))):

                #permutations('ABCD', 2) AB AC AD BA BC BD CA CB CD DA DB DC

            count =1    #투입할 친구의 수
            #해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]

            #시작점부터 모든 취약 지점 확인
            for index in range(start, start + length):
                if position < weak[index]:  #점검할 수 있는 위치를 벗어난 경우
                    count+= 1   #새로운 친구 투입
                    if count > len(dist):   #더 투입이 불가능한 경우
                        break
                    position = weak[index] + friends[count -1]
            answer = min(answer, count) #최소값 계산
    if answer > len(dist):
        return -1
    return answer
