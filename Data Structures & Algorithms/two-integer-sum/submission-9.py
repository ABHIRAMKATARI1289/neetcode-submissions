class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h1 = {}
        for i in range(len(nums)) :
            if target - nums[i] in h1 and h1[target-nums[i]] != i :
                return [h1[target-nums[i]],i]
            h1[nums[i]] = i 
        return []