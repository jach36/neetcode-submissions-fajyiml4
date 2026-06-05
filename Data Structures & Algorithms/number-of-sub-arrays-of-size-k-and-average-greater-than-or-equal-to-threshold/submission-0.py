class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        summ = sum(arr[:k-1])
        res = 0

    
        for l in range(len(arr) - k + 1):
            summ += arr[r]
            if summ / k >= threshold:
                res += 1
            summ -= arr[l]
            r += 1
        return res