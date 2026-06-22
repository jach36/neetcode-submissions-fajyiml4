class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        store = {}

        for s in strs:
            sorted_ = "".join(sorted(s))
            if sorted_ not in store.keys():
                store[sorted_] = [s]
            else:
                store[sorted_].append(s)
        
        for r in store:
            res.append(store[r])
            
        return res
