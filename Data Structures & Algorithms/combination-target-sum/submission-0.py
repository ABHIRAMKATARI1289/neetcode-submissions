class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i,total,fin):
            if total == target :
                res.append(fin.copy())
                return
            elif i >= len(nums):
                return 
            elif total > target :
                return 
            
            fin.append(nums[i])
            dfs(i,total + nums[i], fin)
            fin.pop()
            dfs(i+1,total,fin)
        res = []
        dfs(0,0,[])
        return res 
    
