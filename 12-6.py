#기둥과 보 설치 #x, y 헷갈리지 않게 주의
#https://school.programmers.co.kr/learn/courses/30/lessons/60061?language=python3

def check(build_info):
    for x, y, a in build_info:
        if a == 0: #기둥의 경우
            if y == 0:  #바닥에 있는 경우
                continue    #break 쓰지 말것

            if [x, y, 1] in build_info or [x-1, y, 1] in build_info: # 다른 보의 위
                continue

            if [x, y-1, 0] in build_info:   #다른 기둥의 위
                continue
            return False
        
        elif a == 1: #보의 경우
            if [x, y-1, 0] in build_info or [x+1, y-1, 0] in build_info:    #다른 기둥의 위인 경우
                continue

            if [x-1, y, 1] in build_info and [x+1, y, 1] in build_info:     #다른 보와 양 옆이 연결 된 경우
                continue
            return False

    return True


def solution(n, build_frame):
    build_info= []

    for frame in build_frame:
        x, y, a, b = frame

        if b == 0:  #삭제
            build_info.remove([x, y, a])
            if not check(build_info):
                build_info.append([x, y, a])

        elif b == 1:    #삽입
            build_info.append([x, y, a])
            if not check(build_info):
                build_info.remove([x, y, a])
    
    build_info.sort()
    return build_info



