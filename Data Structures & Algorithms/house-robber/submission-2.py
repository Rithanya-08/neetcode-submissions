from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize = None)
        def solve(i:int) -> int:
            if(i>len(nums)-1):
                return 0
            
            summ1 = solve(i+1)
            summ2 = nums[i] + solve(i+2)
            return max(summ1,summ2)
        return solve(0)