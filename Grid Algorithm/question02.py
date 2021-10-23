"""
<문제> 곱하기 혹은 더하기
    - 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
    'x'혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
    단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽부터 순서대로 이루어 진다고 가정합니다.
    - 예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 (((0+2)x9)x8)x4 = 576
"""

# 내 풀이
# n = input()
#
# number_list = list()
# for temp in n:
#     number_list.append(int(temp))
#
# result = number_list[0]
# i = 0
# while True:
#     if len(number_list) < 2:
#         result = number_list[0]
#         break
#
#     if number_list[i] * number_list[i+1] > number_list[i] + number_list[i+1]:
#         result += (number_list[i] * number_list[i+1])
#     elif number_list[i] * number_list[i+1] < number_list[i] + number_list[i+1]:
#         result += (number_list[i] + number_list[i + 1])
#
#     if i == len(number_list) - 2:
#         break
#
# print(result)


# 정답
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)