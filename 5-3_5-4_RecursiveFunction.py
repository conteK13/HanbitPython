"""def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()"""

def recursive_function(i):
    print(i)
    if i == 100: #i가 100이 되는 순간까지라는 종료 조건을 명시
        return
    recursive_function(i+1)


recursive_function(1)