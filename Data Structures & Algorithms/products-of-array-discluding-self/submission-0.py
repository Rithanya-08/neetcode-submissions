class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        count = 0
        for i in nums:
            if(i!=0):
                total *= i
            else:
                count += 1

        res = []
        for j in nums:
            if(count>=2):
                res.append(0)
            else:
                if(j == 0):
                    res.append(total)
                elif(count == 1 and j !=0 ):
                    res.append(0)
                else:
                   res.append(int(total/j))


        return res