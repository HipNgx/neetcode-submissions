class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0,1
        while l < r < len(numbers) :
            if numbers[l] + numbers[r] == target :
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target :
                l += 1
                r = l + 1
            elif numbers[l] + numbers[r] < target and r == len(numbers) -1 :
                l += 1
                r = l + 1
            else :
                r += 1
        return [l+1, r+1]