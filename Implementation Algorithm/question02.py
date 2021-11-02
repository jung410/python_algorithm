

n = int(input())

"""

# 1시간동안 나올 수 있는 3이 포함된 시간
# 0~59분 0~59초
count = 0
# 1분동안 나올 수 있는 3이 포함된 초
for i in range(60):
    temp = []
    for _data in str(i):
        temp.append(_data)

    for temp_data in temp:
        if temp_data == '3':
            count += 1
            break


print(count * 60)

"""

# 완전탐색 구현문제
# 24 * 60 * 60 = 86400
# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)