s = "aabbaccc"          #s=input()

def solution(s):
    answer = len(s)     #문자열 s의 길이를 초기값으로 넣어둠

    for step in range(1, len(s)//2 +1): #문자열을 나누는 단위는 문자열의 길이의 절반과 같거나 작다
        compressed = ""     #str이 아닌 list로 설정하면, len이 글자수가 아니라 step별로 나눈 글자 수가 된다.
        prev = s[0:step]
        count = 1           #count 초기값은 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count+=1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
result = solution(s)

print(result)


"""
compressed += str(count) + prev if count >= 2 else prev

if count >= 2:
    compressed += str(count)
compressed += prev

"""