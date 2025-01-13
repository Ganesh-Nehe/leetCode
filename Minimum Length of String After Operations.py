class Solution:
    def minimumLength(self, s: str) -> int:
        cc = [0] * 26
        for char in s:
            cc[ord(char) - ord('a')] += 1
        ans = 0
        for count in cc:
            if count == 0:
                continue
            ans += 2 if count % 2 == 0 else 1
        
        return ans