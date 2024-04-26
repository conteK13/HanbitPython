#괄호 변환
#https://school.programmers.co.kr/learn/courses/30/lessons/60058

def balanced_string(p):
    count = 0
    index = 0

    for index in range(len(p)):
        if p[index] == "(":    
            count += 1
        else:
            count -= 1

        if count == 0:
            return index

def check_string(p):    #균형잡힌 괄호 문자열을 입력받는다는 전재
    count = 0
    for i in p:
        if i == "(":
            count += 1
        
        else:
            count -=1
            if count < 0:
                return False
            
    return True


def solution(p):
    answer = ''
    if p == '':     #1.빈문자열인 경우
        return answer
    
    index = balanced_string(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_string(u):
        answer += u
        answer += solution(v)
    
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        
        answer += "".join(u)
    return answer