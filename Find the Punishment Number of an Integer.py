class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(num_str, target, start):
            if start == len(num_str):
                return target == 0
            
            for end in range(start + 1, len(num_str) + 1):
                part = int(num_str[start:end])
                if part > target:
                    break
                if canPartition(num_str, target - part, end):
                    return True
            
            return False

        punishment_sum = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if canPartition(square_str, i, 0):
                punishment_sum += i * i
        
        return punishment_sum