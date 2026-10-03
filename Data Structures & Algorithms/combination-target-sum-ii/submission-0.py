class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = [] 
        def solve(i,temp,target):
            if(target == 0):
                result.append(temp[:])
                return

            if(i>= len(candidates) or target<0):
                return 

            for j in range(i,len(candidates)):
                if(j==i or candidates[j] != candidates[j-1]):
                    temp.append(candidates[j])
                    solve(j+1,temp,target-candidates[j])
                    temp.pop()

        solve(0,[],target)
        return result