class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sortPiles = sorted(piles)
        if h <= len(piles) :
            return(sortPiles[-1])
        l, r = 1, sortPiles[-1]
        res = []
        while l < r :
            hours = 0
            mid = (l+r)//2
            for x in sortPiles :
                if x < mid :
                    hours += 1
                elif x % mid == 0 :
                    hours += (x//mid)
                else :
                    hours += (x//mid + 1)
            if hours <= h :
                res.append(mid)
                r = mid
            else :
                l = mid + 1
        res.sort()
        return res[0]