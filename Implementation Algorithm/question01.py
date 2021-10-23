"""
- 시물레이션 구현 문제
<문제> 상하좌우
    -
"""

n = int(input())
data = list(map(str, input().split()))

#     동  북  서  남
#     R   U  L  D
#     0   1  2  3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
position = [0, 0]

for direction in data:
    if direction == 'R':
        if position[1] + dy[0] > n:
            continue
        position[0] = position[0] + dx[0]
        position[1] = position[1] + dy[0]
    if direction == 'U':
        if position[0] + dx[1] < 0:
            continue
        position[0] = position[0] + dx[1]
        position[1] = position[1] + dy[1]
    if direction == 'L':
        if position[1] + dy[2] > 0:
            continue
        position[0] = position[0] + dx[2]
        position[1] = position[1] + dy[2]
    if direction == 'D':
        if position[0] + dx[3] > n:
            continue
        position[0] = position[0] + dx[3]
        position[1] = position[1] + dy[3]

print(position[0]+1, position[1]+1)