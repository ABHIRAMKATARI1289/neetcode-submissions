class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [[]for _ in range(n)]
        r = [[] for _ in range(n)]
        l[0] = nums[0]
        r[-1] = nums[-1]
        for i in range(1,len(nums)):
            l[i] = l[i-1] * nums[i]
        for i in range(len(nums)-2,-1,-1):
            r[i] = r[i+1] * nums[i]
        print(l)
        print(r)
        res = [[] for _ in range(n)]
        for i in range(1,len(nums) -1):
            res[i] = l[i-1] * r[i+1]
        res[0] = r[1]
        res[-1] = l[-2]
        return res 