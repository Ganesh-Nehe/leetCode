class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_bits = bin(num2).count('1')
        
        x = 0
        for i in range(31, -1, -1):
            if num2_bits > 0 and (num1 & (1 << i)):
                x |= (1 << i)
                num2_bits -= 1        
        for i in range(32):
            if num2_bits == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                num2_bits -= 1
        
        return x