#-*- encoding: utf8 -*-
# n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력

def pair_person(list):
    n = len(list)
    for i in range(n):
        for j in range(i+1, n):
            print(list[i] + ' - ' + list[j])


list_1 = ["dahye", "jiin", "hyojin", "hyunjung"]
print(pair_person(list_1))