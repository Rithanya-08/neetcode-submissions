from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(arr):
            @lru_cache(maxsize = None)
            def solve(i:int) -> int:
                if(i>len(arr)-1):
                    return 0
                take = arr[i] + solve(i+2)
                leave = solve(i+1)
                return max(take,leave)
            return solve(0)
        return max(dp(nums[1:]),dp(nums[:-1]))