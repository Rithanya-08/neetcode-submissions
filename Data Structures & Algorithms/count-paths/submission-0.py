class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1
        result = 0

        def solve(i,j):
            if(i<0 or i>=m):
                return 0
            if(j<0 or j>= n):
                return 0

            if(dp[i][j] != 0):
                return dp[i][j]

            up = solve(i-1,j)
            side = solve(i,j-1)

            dp[i][j] = up + side 

            return dp[i][j]
            
        solve(m-1,n-1)
        return dp[m-1][n-1]