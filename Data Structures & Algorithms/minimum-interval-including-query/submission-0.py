from heapq import heapify, heappush
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        intervals.sort(key = lambda x : x[0])

        for q in queries:
            min_heap = []
            heapify(min_heap)
            for interval in intervals:
                if interval[0] > q:
                    break
                elif interval[1] < q:
                    continue
                else: 
                    length = interval[1] - interval[0] + 1 
                    heappush(min_heap, length)
            try:
                x = min_heap[0] 
            except Exception:
                x = -1
            res.append(x)
        return res
        