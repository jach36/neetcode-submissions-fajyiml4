class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        closeToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        res = []

        for c in s:
            if c in closeToOpen:
                if res and res[-1] == closeToOpen[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return len(res) == 0