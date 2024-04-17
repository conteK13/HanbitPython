#럭키 스트레이트

n=input()
length = len(n)//2
result = 0
for i in n[:length]:
    result += int(i)

for i in n[length:]:
    result -= int(i)

if result == 0:
    print("LUCKY")
else:
    print("READY")