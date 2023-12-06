
#dfs 파악을 위한 print문과 주석
def dfs(graph, v, visited):         #graph:노드간 연결 정보 / v:노드 현재 위치 / visited:방문 여부 확인 리스트
    visited[v] = True               #v 노드 방문 표시
    #print(v, end = ' ')
    print("새로 방문한 노드 :",v, " / 연결된 노드 :", graph[v])
    #현재 노드와 연결된 노드들 확인

    for i in graph[v]:                                          #해당 노드와 연결된 노드들로 반복문을 돌린다.
        print("현재 노드 :", v)
        if not visited[i]:                                      #visited[i] == False (그 노드에 방문한적 없다면) 재귀함수 실행
            print(i, "노드 연결 성공")                          #방문한적 없는 노드를 찾은 경우 재귀 함수 실행
            dfs(graph, i, visited)
        else:
            print(i, "노드 연결 실패")                          #방문한적 있는 노드를 찾은 경우 for문 내 다음 변수로 넘어간다

    print(v, "노드 이전으로 롤백")                     #for문으로 모두 확인 했으나 새로운 노드를 찾지 못한 경우, 이전 노드로 돌아간다.
    
    # 현재 노드의 이전단계로 이동할때, 이전 노드가 어디인지 파악하는 방법은 없을까?


"""    
def dfs(graph, v, visited):         #graph:노드간 연결 정보 / v:노드 현재 위치 / visited:방문 여부 확인 리스트
    visited[v] = True               #v 노드 방문 표시
    print(v, end = ' ')

    for i in graph[v]:                                          #해당 노드와 연결된 노드들로 반복문을 돌린다.
        if not visited[i]:                                      #visited[i] == False (그 노드에 방문한적 없다면) 재귀함수 실행                         
            dfs(graph, i, visited)                              #방문한적 없는 노드를 찾은 경우 재귀 함수 실행
                                                                #방문한적 있는 노드를 찾은 경우 for문 내 다음 변수로 넘어간다

    #for문으로 모두 확인 했으나 새로운 노드를 찾지 못한 경우, 이전 노드로 돌아간다.
"""                                                           


#노드간 연결 정보를 인접리스트(Adjacency List)로 표현
graph = [
    [],         #노드 0과 연결된 노드 없음
    [2, 3, 8],  #노드 1과 연결된 노드 작성
    [1, 7], 
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1,7]
]

visited = [False] * 9   #노드 0부터 노드 9까지 방문 여부를 확인할 리스트


dfs(graph, 1, visited)


"""
result = []
def dfs(graph, v, visited):
#graph:노드간 연결 정보 / v:현재 위치(노드) / visited:방문 여부 확인 리스트
    visited[v] = True           #v번 노드 방문 확인
    #print(v, end = ' ')
    print("새로 방문한 노드 :",v)
    global result
    result.append(v)
    print(result)

    for i in graph[v]:          #해당 노드와 연결된 노드들로 반복문을 돌린다.
        print("현재 노드", v, " / 연결된 노드 :", graph[v])
        if not visited[i]:      #visited[i] == False (그 노드에 방문한적 없다면) 재귀함수 실행
            print(i, "노드로 이동")
            dfs(graph, i, visited)
        else:
            print(i, "연결 실패")
    print(v, "이전 노드로 롤백", sep ='')
    


#노드간 연결 정보를 인접리스트(Adjacency List)로 표현
graph = [
    [],         #노드 0과 연결된 노드 없음
    [2, 3, 8],  #노드 1과 연결된 노드 작성
    [1, 7], 
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1,7]
]

visited = [False] * 9   #노드 0부터 노드 9까지 방문 여부를 확인할 리스트


dfs(graph, 1, visited)
"""