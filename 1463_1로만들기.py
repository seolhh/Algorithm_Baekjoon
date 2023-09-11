N = int(input())

dp = [0]*(N+1)


for i in range(2,N+1):
    dp[i] = dp[i-1]+1    # +1하는 경우는 무조건 가능하니까
    # print(dp[i])
    if i%2 ==0:
        dp[i] = min(dp[i] , dp[i//2]+1)   # dp[i]는 우선 dp[i-1]+1의 값은 항상 가능한데 %2가 가능한 경우엔 두 값음 중 최소값을 넣
    # print(dp[i//2]+1)
    if i%3 ==0:
        dp[i] = min(dp[i] , dp[i//3] +1)

ans = dp[N]


print(ans)