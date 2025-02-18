class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        num = 1
        
        for ch in pattern + 'I': 
            stack.append(str(num))
            num += 1
            
            if ch == 'I':
                while stack:
                    result.append(stack.pop())
        
        return "".join(result)