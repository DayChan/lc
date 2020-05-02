class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        start是开始点，end是从开始点开始能到达的最后一点，tank代表从点start到i+1又想中剩余的油量
        如果tank>=0, 那么能到达i+1， 所以end = i+1。 如果tank<0 说明从start最多到i（end）到不了i+1，
        那么就从下一站从新开始计数（start=end=i+1）. 为什么是下一站, 而不是之前的某站呢? 因为start能到start和i之间任何一点，
        如果在start和i之间存在一点能到i+1，那么， start也能到i+1
        debt代表所有欠下的油，最后如果能还清，那么说明从start走能afford起所有之前can't afford起的路
        """
        start = 0
        end = 0
        tank = 0
        debt = 0
        for i in range(len(gas)):
            tank += gas[i%len(gas)]
            tank -= cost[(i)%len(gas)]
            if tank >= 0:
                end = (i+1)%len(gas)
            else:
                debt += tank
                tank = 0
                start = (i+1)%len(gas)
                end = (i+1)%len(gas)
        if tank + debt >= 0:
            return start
        else:
            return -1