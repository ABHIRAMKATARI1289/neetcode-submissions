class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        love = set(nums)

        res = 1
        cnt = 1  
        
        for n in love :
            if n - 1 not in love :
                cnt = 1 
                while n + cnt in love :
                    cnt += 1 
            res = max(res,cnt)

        return res      