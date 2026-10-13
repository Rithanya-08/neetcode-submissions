from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse = True)
        print(piles)
        def solve(k):
            hours = 0 
            for i in piles:
                hours += ceil(i/k)

            return hours

        low = 1
        high = max(piles)

        while(low<high):
            mid = (high + low) // 2
            x = solve(mid)
            if(x<=h):
                high = mid 
            else:
                low = mid + 1


        return low

        