#-*- endcoding: utf8 -*-
# 재귀호출로 숫자 n개 중에서 최댓값 찾기

# 기존코드
# def find_max_value(list):
#     n = len(list)
#     max = list[0]
#     for i in range(n-1):
#         if max < list[i+1]:
#             max = list[i+1]
#     return max
#
# print(find_max_value([1, 6, 0, 10]))


# 종료 조건: 자료 값이 한 개면(n = 1) 그 값이 최댓값
# 재귀 호출 조건: n개 자료 중 최댓값은 n-1개 자료 중 최댓값과 n-1번째 위치한 값 중 더 큰 값
def recursive_max_value(list, n):
    if n == 1:
        return list[0]
    max = recursive_max_value(list, n-1)
    if max > list[n-1]:
        return max
    else:
        return list[n-1]

list_1 = [1, 2, 0, 50, 999, 123]
print(recursive_max_value(list_1, len(list_1)))
list_2 = [1]
print(recursive_max_value(list_2, len(list_2)))