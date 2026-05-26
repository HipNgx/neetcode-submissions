class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)
        for i in range (1,n -1 ) :
            l = 0
            r = n - 1
            while l < i < r :
                a = [nums[l], nums[i], nums[r]]
                if nums[l] + nums[r] + nums[i] > 0 :
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0  :
                    l += 1
                else :
                    if a not in res :
                        res.append([nums[l], nums[i], nums[r]])
                    l += 1
        return res
