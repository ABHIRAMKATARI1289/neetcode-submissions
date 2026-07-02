class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) -1 

        while l < r :
            mid = l + (r-l)//2
            if mid < len(nums) -1 and nums[mid] > nums[mid+1] :
                return nums[mid+1]
            else :
                if nums[mid] < nums[r]:
                    r = mid
                else : 
                    l = mid + 1 
        return nums[l]
    