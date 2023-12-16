# 최소공배수는 a,b 모두의 배수인 자연수 중 제일 작은 수
# answer = a의 배수 이면서 b의 배수

# input
n = int(input())

def gcd(a, b):
    if b == 0:
        # 더이상 나눌게 없으면 a가 도출 = 최대공약수
        return a
    else:
        return gcd(b, a%b)

for i in range(n):
    a, b = map(int, input().split())
    answer = a * b // gcd(a, b)
    print(answer)
