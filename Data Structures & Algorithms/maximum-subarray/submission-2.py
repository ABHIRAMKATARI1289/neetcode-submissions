class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [nums[0]]*n 

        for i in range(n):
            res = nums[i]
            dp[i] = max(dp[i],res)
            j = i + 1
            while j < n :
                res += nums[j]
                dp[j] = max(dp[j],res)
                j += 1 
        return max(dp)
                
        