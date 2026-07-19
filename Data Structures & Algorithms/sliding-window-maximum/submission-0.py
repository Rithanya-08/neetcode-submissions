class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = k-1
        lst = []

        while(j<len(nums)):
            lst.append(max(nums[i:j+1]))
            i+=1
            j+=1

        return lst

