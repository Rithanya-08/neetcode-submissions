class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l3 != l1 + l2:
            return False

        dp = [[None] * (l2 + 1) for _ in range(l1 + 1)]

        def solve(i, j):
            if i == l1 and j == l2:
                return True
            if dp[i][j] is not None:
                return dp[i][j]

            k = i + j
            res = False
            if i < l1 and s1[i] == s3[k] and solve(i + 1, j):
                res = True
            elif j < l2 and s2[j] == s3[k] and solve(i, j + 1):
                res = True

            dp[i][j] = res
            return res

        return solve(0, 0)