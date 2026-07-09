class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tot = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(tot.copy())
                return
            
            tot.append(nums[i])
            dfs(i+1)
            tot.pop()
            j = i + 1 
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j)
    
        dfs(0)
        return res 