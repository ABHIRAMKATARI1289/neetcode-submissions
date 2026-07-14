class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in pair :
                return [pair[comp],i]
            pair[num] = i 
