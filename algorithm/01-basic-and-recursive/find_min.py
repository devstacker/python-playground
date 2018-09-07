#-*- encoding: utf8 -*-s
#숫자 n개를 리스트로 입력받아 최솟값 출력

def find_min(list):
    n = len(list)
    min = list[0]
    for i in range(n-1):
        if min > list[i+1]:
            min = list[i+1]
    return min


list_1 = [45, 66, 79, 12, 1]
print(find_min(list_1))
list_2 = [1, 0, 2, 3, 4, 5, 6]
print(find_min(list_2))