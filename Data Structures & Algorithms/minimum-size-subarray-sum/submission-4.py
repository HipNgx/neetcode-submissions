class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(x for x in nums) < target :
            return 0
        if target in nums :
            return 1
        if target < max(x for x in nums) :
            return 1
        l, r = 0,1
        res = []
        sumTemp = nums[0]
        while l < r < len(nums) :
            sumTemp += nums[r]
            while sumTemp >= target :
                res.append(len(nums[l:r+1]))
                sumTemp -= nums[l]
                l += 1
            r += 1
        return min(x for x in res)