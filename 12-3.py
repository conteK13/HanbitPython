s = "aabbaccc"

def solution(s):
    result = len(s)

    for step in range(1, len(s)//2 +1):
        compress = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compress += str(count) + prev if count >=2 else prev
                prev = s[j:j+step]
                count = 1
                
        compress += str(count) + prev if count >=2 else prev
        result = min(result, len(compress))
    return result

s = "aabbaccc"
result = solution(s)
print(result)