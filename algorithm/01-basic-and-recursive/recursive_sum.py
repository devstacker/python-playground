#-*- endcoding: utf8 -*-
# 재귀호출로 1부터 n까지의 합 구하기

def recursive_sum(n):
    if n == 0:
        return n
    return n + recursive_sum(n-1)

print(recursive_sum(3))
print(recursive_sum(10))
print(recursive_sum(0))