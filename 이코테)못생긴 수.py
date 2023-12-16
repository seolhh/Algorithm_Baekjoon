n = int(input())

ugly = [0] * (n+1)  # 못생긴 수를 담기 위한 테이블
print(ugly)
ugly[1] = 1 # 첫번째 못생긴 수 = 1
print(ugly)
i2 = i3 = i5 = 0   # 2배, 3배, 5배를 위한 인덱스
next2, next3, next5 = 2, 3, 5  # 처음에 곱셈 값을 초기화  -> 이게 뭔소리임?

# 1부터 n까지의 못생긴 수 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중 가장 작은 수 선택
    ugly[l] = min(next2, next3, next5)
    print(ugly[l])
    if ugly[l] == next2:
        i2 += 1
        # print(ugly)
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])