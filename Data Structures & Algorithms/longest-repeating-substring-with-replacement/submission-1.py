class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        store = {}
        l = r = 0

        for r in range(len(s)):
            store[s[r]] = 1 + store.get(s[r], 0)

            if (r - l + 1) - max(store.values()) > k:
                store[s[l]] -= 1
                l += 1
            else:
                res = max(r - l + 1, res)
        return res
