class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i 
        
        size, end = 0, lastIndex[s[0]]
        res = []
        start = 0
        for d, n in enumerate(s):
            size += 1
            if lastIndex[n] > end:
                end = lastIndex[n]

            print("last: ", lastIndex[n], " \nend: ", end, "\nsize: ", size, "\n")
            if size > end - start:
                res.append(size)
                size = 0
                start = end + 1
        return res