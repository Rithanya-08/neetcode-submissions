class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        n = len(coins)

        def solve(i,rem):
            if(rem == 0):
                return 1
            if(rem<0 or i>=n):
                return 0

            if((i,rem) in dp):
                return dp[(i,rem)]

            take = solve(i,rem - coins[i])
            skip = solve(i+1,rem)

            dp[(i,rem)] = take + skip 
            return dp[(i,rem)]
            
        return solve(0,amount)