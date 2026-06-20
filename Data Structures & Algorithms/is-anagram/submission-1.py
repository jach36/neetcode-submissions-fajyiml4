class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        store = list(s)


        for first in t:
            if first in store:
                store.remove(first)
            else:
                return False
        return True