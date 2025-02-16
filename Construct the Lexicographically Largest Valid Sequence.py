class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        result = [0] * length
        used = set()

        def backtrack(index: int) -> bool:
            if index == length:
                return True
            
            if result[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if num in used:
                    continue
                
                if num == 1:
                    result[index] = num
                    used.add(num)
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used.remove(num)
                else:
                    second_index = index + num
                    if second_index < length and result[second_index] == 0:
                        result[index] = result[second_index] = num
                        used.add(num)
                        if backtrack(index + 1):
                            return True
                        result[index] = result[second_index] = 0
                        used.remove(num)
            
            return False
        
        backtrack(0)
        return result