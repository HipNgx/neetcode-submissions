class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(temperatures) :
            warmer = False
            count = 0
            for y in range(i + 1, len(temperatures)) :
                count += 1
                if temperatures[y] > temperatures[i] :
                    res.append(count)
                    warmer = True
                    break
            if not warmer :
                res.append(0)
            i += 1
        return res