class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(x for x in nums) < target :
            return 0
        l, r = 0,0
        res = []
        sumTemp = 0
        while r < len(nums) :
            sumTemp += nums[r]
            if sumTemp >= target :
                res.append(len(nums[l:r+1]))
                sumTemp = 0
                l += 1
                r = l
            else :
                r += 1
        return min(x for x in res)