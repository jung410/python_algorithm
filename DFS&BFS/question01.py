"""
음료수 얼려 먹기
- 연결 요소 찾기

세로길이 N과 가로길이 M이 주어진다.
구멍이 뚫려있으면 0, 뚫려있지 않다면 1
"""

"""
그래프 형태로 모델링할 수 있다.

DFS를 활용하는 알고리즘
"""


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


# DFS로 특정 노드를 방문하고, 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)



