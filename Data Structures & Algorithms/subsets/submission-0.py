class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def saved(i) :
            if i >= len(nums) :
                res.append(Stack.copy())
                return
            Stack.append(nums[i])
            saved(i+1)
            Stack.pop()
            saved(i+1)
        res = []
        Stack = []
        saved(0)
        
        return res