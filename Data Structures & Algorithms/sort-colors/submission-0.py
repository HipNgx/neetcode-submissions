class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1 ):
            swap = False
            for y in range (len(nums) - i -1) :
                if nums[y] > nums[y+1] :
                    nums[y], nums[y+1] = nums[y+1], nums[y]
                    swap = True
            if not swap :
                break