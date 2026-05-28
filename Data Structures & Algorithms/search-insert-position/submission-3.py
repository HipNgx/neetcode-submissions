class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1] :
            return len(nums)
        if target <= nums[0] :
            return 0
        n = len(nums)
        l, r = 0, n-1
        while l < r :
            mid = (l+r) //2
            if r - l == 1 :
                return r
            if target == nums[mid] :
                return mid
            elif target > nums[mid] :
                l = mid
            else :
                r = mid