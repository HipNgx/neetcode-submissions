class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :
            return 0
        if x == 1 :
            return 1
        l, r = 0, x 
        while l < r :
            mid = (l + r) // 2
            if mid ** 2 == x :
                return mid
            elif mid ** 2 < x :
                if (mid + 1) ** 2 > x :
                    return mid
                l = mid
            else :
                if (mid - 1) ** 2 < x :
                    return mid - 1
                r = mid