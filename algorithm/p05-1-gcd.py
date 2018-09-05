#-*- encoding: utf8 -*-
# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수


def gcd(a, b):
    i = min(a, b)  # 두 수 중에서 최솟값을 구하는 파이썬 함수
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1  # i를 1만큼 감소시킴


print(gcd(1, 5))  # 1
print(gcd(3, 6))  # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27


# 유클리드 방식을 이용한 최대공약수 구하기(종료조건:‘어떤 수와 0의 최대공약수는 자기 자신’. 즉, b가 0이면 재귀 호출을 멈추고 결과를 돌려줌).

def gcd(a, b):
    if b == 0:  # 종료 조건
        return a
    return gcd(b, a % b)  # 좀 더 작은 값으로 자기 자신을 호출


print(gcd(1, 5))  # 1
print(gcd(3, 6))  # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27