N = int(input())

dp = [0]*(N+1)


for i in range(2,N+1):
    dp[i] = dp[i-1]+1    # +1하는 경우는 무조건 가능하니까
    # print(dp[i])
    if i%2 ==0:
        dp[i] = min(dp[i] , dp[i//2]+1)   ## 왜 +1을 해주는거지?
    # print(dp[i//2]+1)
    if i%3 ==0:
        dp[i] = min(dp[i] , dp[i//3] +1)

ans = dp[N]


print(ans)