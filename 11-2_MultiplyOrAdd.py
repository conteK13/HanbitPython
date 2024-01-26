import time

s = input()
start_time = time.time()
result= int(s[0]) 

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

end_time = time.time()
print("time : ", end_time-start_time)


"""
#매번 int 함수를 사용하는 방법.. 어떻게 개선하면 좋을까
s = input()
start = int(s[0]) 
result = start


for i in s[1:]:
    if int(start) <= 1 or int(i) <= 1:      #1보다 같거나 작으면 덧셈을 하는 게 더 큰 수를 만들 수 있음
        result += int(i)            
    else:
        result *= int(i)
    start = i

print(result)
"""
