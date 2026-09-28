class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = (len(nums1) + len(nums2))
        half = math.ceil(length/2) 
        print(half)
        i = j = 0 
        even = False
        if(length %2 == 0):
            even = True
        result = []

        while((even == True and half >= 0) or (even == False and half > 0)):
            if(i<len(nums1) and j < len(nums2) and nums1[i]<nums2[j]):
                result.append(nums1[i])
                i+=1
            elif(i<len(nums1) and j < len(nums2) and nums1[i]>nums2[j]):
                result.append(nums2[j])
                j+=1
            elif(i<len(nums1)):
                result.append(nums1[i])
                i+=1
            elif(j<len(nums2)):
                result.append(nums2[j])
                j+=1
            half -= 1

        if(even == True):
            return (result[-1] + result[-2]) /2.0
        else:
            return result[-1]