#문자열 뒤집기

s= input()
group = 1

start = s[0]
for i in range(len(s)):
    if start != s[i]:
        group += 1
        start= s[i]

result = group//2   #int(group/2) 로 써도 괜찮
print(result)