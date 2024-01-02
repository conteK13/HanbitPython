#원소의 개수 n을 입력받지 않고 len(array)로 처리하는 코드

def sequential_serch(arget, array): #target은 찾고자 하는 문자열, array는 문자열의 배열(목록)
    for i in range(len(array)):
        if array[i] == target:
            return i + 1 #현재위치 반환(0부터 시작하니까 1을 offset으로 보상)
        

print("찾을 문자열을 입력하세요.")
target= input()

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_serch(target, array))



"""
def sequential_serch(n, target, array): #n은 원소의 개수, target은 찾고자 하는 문자열, array는 문자열의 배열(목록)
    for i in range(n):
        if array[i] == target:
            return i + 1 #현재위치 반환(0부터 시작하니까 1을 offset으로 보상)
        

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_serch(n, target, array))
"""