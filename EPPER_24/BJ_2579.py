# 계단오르기
n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * (n)

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = s[2] + max(s[0], s[1])

for i in range(3, n):
    dp[i] = s[i] + max(dp[i-2], s[i-1] + dp[i-3])

print(dp[n-1])


def solution(n, score):
    dp = [0] * 301

    dp[1] = score[1]
    dp[2] = score[1] + score[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + score[i -1], dp[i-2]) + score[i]

    return dp[n]