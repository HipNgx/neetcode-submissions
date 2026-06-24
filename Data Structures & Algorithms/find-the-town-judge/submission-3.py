class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        believed = {}
        believing = {}
        for i in trust :
            if i[0] not in believing :
                believing[i[0]] = 1
            else :
                believing[i[0]] += 1
            if i[1] not in believed :
                believed[i[1]] = 1
            else :
                believed[i[1]] += 1
        for i in believed :
            if believed[i] == n-1 and i not in believing :
                return i
        return -1 

            
                

