class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        lst = []

        i = 0 
        while(i<len(nums)):
            if(i>0 and i<len(nums)-1 and nums[i]==nums[i-1]):
                i+=1
                continue
            l = i+1
            r = len(nums)-1
            target = -nums[i]

            while(l<r):
                if(target == nums[l]+nums[r]):
                    lst.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
                
                    while(l<r and nums[r] == nums[r+1]):
                        r-=1

                elif(nums[l]+nums[r]+nums[i] < 0):
                    l+=1
                else:
                    r-=1

                

            i+=1



        return lst