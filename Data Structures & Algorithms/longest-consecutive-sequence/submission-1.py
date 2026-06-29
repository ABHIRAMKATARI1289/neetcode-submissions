class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        nums.sort()
        i = 1
        res = 1
        cnt = 1  
        print(nums)
        while i < len(nums):
            if nums[i-1] + 1 == nums[i]:
                cnt += 1
            elif nums[i-1] == nums[i] :
                cnt += 0 
            else :
                cnt = 1
            res = max(res,cnt)
            i += 1    
        return res      