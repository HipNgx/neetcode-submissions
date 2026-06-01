class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        l, r = 0, 0
        window = ''
        longest = 0
        count_ = 0

        while r < len(s):
            window += s[r]
            count_ = len(window) - max(window.count(c) for c in set(window))

            if count_ <= k:
                longest = max(longest, len(window))
            else:
                window = window[1:]
                l += 1

            r += 1

        return longest