class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        wasGreater = arr[1] > arr[0] 
        res = 2
        ans = 0 


        for i in range(1, len(arr)):
            greater = arr[i] > arr[i - 1]
            less = arr[i] < arr[i - 1]
            if wasGreater:
                if greater:
                    res = 2
                elif less:
                    res += 1
                else:
                    res = 1
            else:
                if greater:
                    res += 1
                elif less:
                    res = 2
                else:
                    res = 1
            ans = max(ans, res)
            wasGreater = greater
        return ans
