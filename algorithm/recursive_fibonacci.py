#-*- endcoding:utf8 -*-
# 재귀로 피보나치 수열 n번째 값 출력

def recursive_fibo(n):
    if n <= 1:
        return n
    return recursive_fibo(n-2) + recursive_fibo(n-1)

print(recursive_fibo(7))
print(recursive_fibo(10))