class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)-1) :
            min_cur_index = i
            for y in range (i+1, len(nums)) :
                if nums[y] <= nums[min_cur_index] :
                    min_cur_index = y
            nums[i], nums[min_cur_index] = nums[min_cur_index], nums[i]
        return nums