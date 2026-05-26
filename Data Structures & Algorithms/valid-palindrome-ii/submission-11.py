class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        def is_pal(sub_s):
            return sub_s == sub_s[::-1]
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(s[l+1:r+1]) or is_pal(s[l:r])
            l += 1
            r -= 1
        return True