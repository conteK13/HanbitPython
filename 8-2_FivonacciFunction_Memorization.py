"""
#메모리제이션 하기 위한 리스트 크기 설정
n = int(input("몇번째 피보나치 수열을 확인할지 입력하세요 : "))

d = [0] * (n+1)

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    #이미 계산한 적 있다면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(n))
"""


d = [0] *7
c = 0       #함수 동작을 확인하기 위한 카운트 함수

def fibo(x):
    global c
    c += 1
    print("\ncount=", c, 'f(' + str(x) + ')')
    if x == 1 or x == 2:
        print("x = ", x, ", return 하면서 +1 하고 x-1, x-2 에 대한 계산 종료", sep="")
        return 1
    
    #이미 계산한 적 있다면 그대로 반환
    if d[x] != 0:
        print("f(", x, ")은 이미 계산 완료 되었습니다.", sep = "")
        return d[x]
    
    print("x = ", x, ", 이후 x-1과 x-2를 계산할 예정입니다.", sep="")
    d[x] = fibo(x-1) + fibo(x-2)
    print("\nx-2 계산 완료, x=", x, "으로 복귀", sep = "")
    print("x = ", x, ", ", d, sep="")
    return d[x]

print("\n", fibo(6), sep = "")
