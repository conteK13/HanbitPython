#실패율
#https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []     #결과를 return할 리스트
    length = len(stages)    #user의 수

    
    for i in range(1, N+1):
        count = stages.count(i)     #stage 값이 i인 갯수

        if length == 0:             #사람이 x인 경우
            fail = 0
        else:
            fail = count / length   #실패율 = 스테이지에 도달했으나 아직 클리어 못한 플레이어 수 / 스테이지 도달한 플레이어 수

        answer.append((i, fail))    #i는 스테이지의 값, fail은 실패율
        length -= count             #유저수에서 해당 스테이지를 클리어 못한 플레이어 수를 뺀다
    
    answer = sorted(answer, key = lambda t: t[1], reverse= True)
    answer = [i[0] for i in answer]

    return answer

"""N = 5
stages= [2, 1, 2, 6, 2, 4, 3, 3]"""

N = 4
stages= [4, 4, 4, 4, 4]

result = solution(N, stages)
print(result)