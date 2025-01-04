class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        l = [set() for _ in range(n)]
        r = [set() for _ in range(n)]

        for i in range(1, n):
            l[i] = l[i - 1].copy()
            l[i].add(s[i - 1])

        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1].copy()
            r[i].add(s[i + 1])

        unique_palindromes = set()

        for i in range(1, n - 1):  
            for ch in l[i]:
                if ch in r[i]:  
                    unique_palindromes.add(ch + s[i] + ch)
        
        return len(unique_palindromes)