class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        if len(nums) == 1 :
            return 1
        while l <= len(nums)-1 :
            if nums[l] == nums[l-1] :
                nums.remove(nums[l-1])
            else :
                l += 1
        return l