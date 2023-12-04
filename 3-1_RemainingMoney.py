import time

n= 1260
count = 0

coin_types=[500, 100, 50, 10]
start_time = time.time()

for i in coin_types:
    if n // i > 0:
        count += n//i
        n= n%i

end_time = time.time()
print("if문이 추가된 time : ", end_time-start_time)
#이번 코딩은 짧아서 비교가 어렵지만, if문을 불필요하게 추가하는 경우를 줄여야함

print(count)

start_time = time.time()

for i in coin_types:
    count += n//i
    n= n%i

end_time = time.time()
print("if문이 없는 time : ", end_time-start_time)
print(count)
        