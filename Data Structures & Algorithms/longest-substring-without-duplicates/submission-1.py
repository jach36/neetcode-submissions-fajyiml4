class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        res = 0
        if len(s) == 1:
            return 1

        while r < len(s) and l < r:
            substring = set(s[l:r])
            while s[r] in substring and l < r:
                l += 1
                substring.remove(s[r])
                substring = set(s[l:r])
            r += 1
            res = max(len(s[l:r]), res)
        return res