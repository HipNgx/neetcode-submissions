class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for key, val in enumerate(nums) :
            for key2, val2 in enumerate(nums[key + 1:]) :
                if val + val2 == target :
                    ans.append(key)
                    ans.append(key2 + key + 1)
                    return ans