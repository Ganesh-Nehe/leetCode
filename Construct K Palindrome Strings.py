class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible
        if k > len(s):
            return False
        
        # Count the frequency of each character
        char_count = Counter(s)
        
        # Count characters with odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # We need at least `odd_count` palindromes
        return odd_count <= k  