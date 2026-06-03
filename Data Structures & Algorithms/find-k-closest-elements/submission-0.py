class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr) :
            return arr
        window = [arr[x] for x in range(len(arr)) if x < k]  
        r = k
        while r < len(arr) :
            if (arr[r] - x) < x - window[0] :
                window = window[1::]
                window.append(arr[r])
            r += 1
        return window
