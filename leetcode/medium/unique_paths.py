class UniquePath:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


up = UniquePath()
print(up.uniquePaths(3, 2))
print(up.uniquePaths(3, 7))
