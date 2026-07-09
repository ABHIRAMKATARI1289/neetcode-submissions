class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(tot):
            if len(tot) == len(nums):
                res.append(tot.copy())
                return 
            for num in nums :
                if num not in tot:
                    tot.append(num)
                    dfs(tot)
                    tot.pop()
        res = []
        dfs([])
        return res 