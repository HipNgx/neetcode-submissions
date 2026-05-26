class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 :
            if nums[0] != target :
                return -1
            else :
                return 0
        n = len(nums) 
        l, r = 0, n
        while l < r :
            mid = (l + r) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                r = mid
            else :
                l = mid + 1
        return -1