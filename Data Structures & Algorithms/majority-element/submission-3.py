class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i in nums :
            if i not in dict :
                dict[i] = 1
            else :
                dict[i] += 1
        for key, value in dict.items() :
            if value > len(nums) // 2 :
                return key
        return 0
