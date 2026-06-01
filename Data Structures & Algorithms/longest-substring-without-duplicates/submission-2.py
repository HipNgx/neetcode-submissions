class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 :
            return 1
        r=0
        window = ''
        longest = 0
        while r < len((s)) :
            if s[r] not in window :
                window += s[r]
            else :
                longest = max(longest, len(window))
                while s[r] in window:
                    window = window[1::]
                window += s[r]
            r += 1
            longest = max(longest, len(window))
        return longest
            
