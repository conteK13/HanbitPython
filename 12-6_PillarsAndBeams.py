def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:   #설치된 것이 '기둥'인 경우
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                #조건 1) y = 0이면 continue
                #조건 2) x
                continue
            return False
        elif stuff ==1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame    #stuff 0 = 기둥, 1 = 보 # operate 0 = 삭제, 1 = 설치
        if operate == 0:                
            answer.remove([x, y, stuff])
            if not possible(answer):    #삭제했는데 조건이 맞지 않으면 다시 추가
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])    #추가했는데 조건에 맞지 않으면 다시 삭제
    return sorted(answer)