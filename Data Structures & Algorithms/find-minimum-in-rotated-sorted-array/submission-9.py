class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r :
            mid = (l+r) // 2
            if len(nums[l:r+1]) <= 3 : 
                return min(nums[l:r+1])
            if nums[mid] > nums[r] and nums[mid] > nums[l] :
                if nums[l] > nums[r] :
                    l = mid + 1
                else :
                    r = mid - 1
            elif nums[mid] < nums[r] and nums[mid] < nums[l] :
                if nums[mid-1] > nums[mid] :
                    return nums[mid]
                else :
                    r -= 1
            elif nums[mid] > nums[l] and nums[mid] < nums[r] :
                return nums[l]
            else :
                return nums[r]