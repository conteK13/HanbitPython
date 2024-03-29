#거스름돈

#n : 거슬러 줘야 할 돈, coin_type : 동전 단위

n = 1260
coin_type = [500, 100, 50, 10]
count = 0

for i in range(len(coin_type)):
    if n // coin_type[i] >= 1:              #if문이 없어도 되나?
        count += n// coin_type[i]
        n = n % coin_type[i]

print(count)