class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1 
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                tank = gas[i] - cost[i]
                t = i + 1 
                while t != i:
                    if t >= len(gas):
                        t = 0 
                        
                    if t == i:
                        return t
                    tank += gas[t]
                    tank -= cost[t]
                    if tank < 0:
                        break 
                    t += 1
                    if t == i:
                        return t
                
        return res