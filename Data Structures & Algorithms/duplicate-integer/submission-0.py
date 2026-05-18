class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = []
        flag = False
        for i in nums :
            if i not in ans :
                ans.append(i)
            else :
                flag = True
        return flag
                