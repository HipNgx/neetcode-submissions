class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # min is in RIGHT half (rotation point is right of mid)
                l = mid + 1
            else:
                # min is in LEFT half including mid
                r = mid

        return nums[l]