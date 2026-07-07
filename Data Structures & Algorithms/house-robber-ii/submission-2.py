class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        def dp(nums):
            s = len(nums)
            dp = [0] * s
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,s):
                dp[i] = max(dp[i-1],dp[i-2] + nums[i])
            return dp[-1]
        l1 = dp(nums[:n-1])
        l2 = dp(nums[1:n])
        return max(l1,l2)