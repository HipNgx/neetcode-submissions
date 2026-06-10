class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r :
            mid = (l+r) // 2
            if len(nums[l:r+1]) < 3 : 
                return min(nums[l:r+1])
            if nums[mid] > nums[r] :
                l = mid + 1
            else :
                r = mid