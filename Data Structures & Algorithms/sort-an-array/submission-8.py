class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)) :
            for y in range (len(nums)-i-1) :
                if nums[y] > nums[y+1] :
                    nums[y], nums[y+1] = nums[y+1], nums[y]
        return nums