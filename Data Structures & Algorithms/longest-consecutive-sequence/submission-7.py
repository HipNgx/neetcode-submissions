class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        if len(nums) == 1 :
            return 1
        nums.sort()
        longest = []
        max_value = 1
        for i in range (len(nums)) :
            longest.append(nums[i])
            for y in range(i, len(nums)-1) :
                if nums[y] == nums[y+1] + 1 or nums[y] == nums[y+1] - 1 :
                    longest.append(nums[y+1])
                    max_value = max(max_value, len(longest))
                elif nums[y] == nums[y+1] :
                            continue
                else :
                    break
            longest = []
        return max_value