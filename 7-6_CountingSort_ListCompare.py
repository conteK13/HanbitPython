n = int(input())
array = [0] * 1000001 #모든 원소의 번호를 포함할수 있는 크기의 리스트

#가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] =1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')