class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = []
        if 0 not in nums :
            for x in nums :
                product = product * x
            for x in range (len(nums)) :
                tempProduct = product
                ans.append(tempProduct // nums[x])
            return ans
        else :
            count_ = 0
            index_0 = []
            for i in range(len(nums)) :
                if nums[i] == 0 :
                    index_0.append(i)
                if len(index_0) > 1 :
                    return [0] * len(nums)
                if nums[i] != 0 :
                    product = product * nums[i]
            for i in range (len(nums)) :
                tempProduct = product
                if i not in index_0 :
                    ans.append(0)
                else :
                    ans.append(tempProduct)
            return ans

        