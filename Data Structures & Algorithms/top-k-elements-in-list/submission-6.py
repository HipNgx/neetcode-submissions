class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        max_frequence = 0
        for i in nums :
            if i not in dict1 :
                dict1[i] = 1
            else :
                dict1[i] += 1
        dict1 = dict(sorted(dict1.items(), key = lambda item : item[1], reverse = True))
        ans = []
        for key, value in dict1.items() :
            ans.append(key)
            k -= 1
            if k == 0 :
                break
        return ans

