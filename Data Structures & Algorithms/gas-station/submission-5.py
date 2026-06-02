class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1 
        for i in range(len(gas)):
            tank = gas[i] - cost[i]
            t = i + 1 
            while tank >= 0:
                if t >= len(gas):
                    t = 0 
                if t == i:
                    return t
                tank += gas[t]
                tank -= cost[t]
                t += 1
                
        return res