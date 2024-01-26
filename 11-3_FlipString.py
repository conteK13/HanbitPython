#경우의 수가 0과 1밖에 없으므로, 책에서 서술 하는 것보다 아래의 코드가 더 적당할 듯

import time

s = input()     #문자열 입력 받기
start_time = time.time()
count = 1       #인접한 위치의 숫자가 동일 할때, 하나의 그룹으로 취급함. 초기값은 1

for i in range(0, len(s)-1):    
    if s[i] != s[i+1]:  #s[i]와 인접한 s[i+1]의 값이 동일 하지 않을 경우
        count += 1      #그룹의 개수를 1추가 한다.

result = int(count/2)   #문자열을 뒤집는 개수는 그룹의 개수를 반으로 나눈 값과 같거나 작다. (0과 1밖에 없기 때문에)
                        #예시-그룹의 개수가 7개일 경우) 0과 1의 그룹의 개수가 3, 4 이므로 result는 3
                        #0.5를 버려야 하므로, round가 아니라 int를 사용
print(result)
end_time = time.time()
print("time : ", end_time-start_time)



"""import time

s = input()     #문자열 입력 받기
start_time = time.time()
count0 = 0      #0으로 바꾸는 경우(지금은 1이라는 소리)
count1 = 0      #1로 바꾸는 경우(지금은 0이라는 소리)

if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
end_time = time.time()
print("time : ", end_time-start_time)

"""

