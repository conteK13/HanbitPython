#가사 검색
#https://school.programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer


"""
def solution(words, queries):
    answer= []  #결과를 저장하기 위함
    
    for query in queries:
        n = len(query)          #query의 총 길이(?포함)
        i = query.find("?")     #query가 처음 등장하는 위치
        c = query.count("?")    #?가 반복되는 횟수
        result = 0

        if i ==0:
            wild = query[c:]
            for word in words:
                if wild == word[c:]:
                    result +=1
        
        else:
            wild = query[:i]
            for word in words:
                if len(word) == n:
                    if wild == word[:i]:
                        result += 1

        answer.append(result)    

    return answer
"""