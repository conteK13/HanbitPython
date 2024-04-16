#곱하기 혹은 더하기

s = input()
result = int(s[0])

for i in range(1, len(s)):
    now = int(s[i])
    if result <= 1 or now <=1:
        result += now
    
    else:
        result = result * now

print(result)