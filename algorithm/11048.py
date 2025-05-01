def max_candies(N,M,candy) :
    dp = [[0] * (M +1) for _ in range(N+1)]

    for i in range(1,N+1) :
        for j in range(1, M+1):
            dp[i][j] = max(
                dp[i-1][j], # 위
                dp[i][j-1], # 왼쪽
                dp[i-1][j-1] # 대각선
            ) + candy[i-1][j-1] # candy list의 현재 사탕수
    return dp[N][M]

N, M = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(N)]

print(max_candies(N,M,candy))
