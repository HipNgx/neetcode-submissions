class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        mid = len(s) // 2
        l = s[:mid]
        r = s[mid::]
        r = r[::-1]
        for x in range (len(l)) :
            if r[x] != l[x] :
                return False
        return True