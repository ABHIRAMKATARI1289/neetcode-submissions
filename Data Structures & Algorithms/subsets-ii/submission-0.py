class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tot = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                if tot not in res :
                    res.append(tot.copy())
                return
            
            tot.append(nums[i])
            dfs(i+1)
            tot.pop()
            dfs(i+1)
    
        dfs(0)
        return res 
        