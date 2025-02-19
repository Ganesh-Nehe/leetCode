class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def is_happy(s):
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))
        
        chars = ['a', 'b', 'c']
        happy_strings = []
        
        for candidate in product(chars, repeat=n):
            s = ''.join(candidate)
            if is_happy(s):
                happy_strings.append(s)
        
        happy_strings.sort()
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""