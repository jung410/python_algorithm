""""""
"""
- 스택 자료구조 : 선입후출 -> 박스쌓기, 입구와 출구가 동일함
    - 파이썬은 list의 append와 pop을 이용하여 구현할 수 있다.(시간복잡도는 O(1))

- 큐 자료구조 : 선입선출 -> 입구와 출구가 모두 뚫려있는 터널과 같은 형태
    - 파이썬은 deque를 사용하도록 하자.
    - 삽입 : append
    - 삭제 : popleft
    
- 재귀함수(Recursive Function) : 자기 자신을 다시 호출하는 함수
"""

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

# DFS 소스코드 예제(재귀함수 사용)
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)