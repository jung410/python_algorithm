"""
왕실의 나이트
"""

n = input()

#     동  북  서  남
#     0   1  2  3
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 동동 북남 001, 003
# 서서 북남 221, 223
# 북북 동서 110, 112
# 남남 동서 330, 332

array = [[0]*8 for i in range(8)]

x = n[0]
y = n[1]

if x == 'a':
    x = 0
elif x == 'b':
    x = 1
elif x == 'c':
    x = 2
elif x == 'd':
    x = 3
elif x == 'e':
    x = 4
elif x == 'f':
    x = 5
elif x == 'g':
    x = 6
elif x == 'h':
    x = 6

position = [int(x), int(y)-1]

direct_list = ['001', '003', '221', '223', '110', '112', '330', '332']
# 동동 북남 001, 003
# 서서 북남 221, 223
# 북북 동서 110, 112
# 남남 동서 330, 332
count = 8
for direct in direct_list:
    temp_position = position.copy()
    for dir in direct:
        temp_dir = int(dir)
        if temp_dir == 0:
            if temp_position[1] + dy[temp_dir] > 7:
                count -= 1
                break
            temp_position[0] = temp_position[0] + dx[temp_dir]
            temp_position[1] = temp_position[1] + dy[temp_dir]
        if temp_dir == 1:
            if temp_position[0] + dx[temp_dir] < 0:
                count -= 1
                break
            temp_position[0] = temp_position[0] + dx[temp_dir]
            temp_position[1] = temp_position[1] + dy[temp_dir]
        if temp_dir == 2:
            if temp_position[1] + dy[temp_dir] < 0:
                count -= 1
                break
            temp_position[0] = temp_position[0] + dx[temp_dir]
            temp_position[1] = temp_position[1] + dy[temp_dir]
        if temp_dir == 3:
            if temp_position[0] + dx[temp_dir] > 7:
                count -= 1
                break
            temp_position[0] = temp_position[0] + dx[temp_dir]
            temp_position[1] = temp_position[1] + dy[temp_dir]


print(count)
