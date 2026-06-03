class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(x for x in nums) < target :
            return 0
        l, r = 0,1
        res = []
        sumTemp = nums[0]
        while l < r < len(nums) :
            while sumTemp >= target :
                res.append(len(nums[l:r]))
                sumTemp -= nums[l]
                l += 1
            sumTemp += nums[r]
            r += 1
        while sumTemp >= target :
            res.append(len(nums[l:r]))
            sumTemp -= nums[l]
            l += 1
        return min(x for x in res)