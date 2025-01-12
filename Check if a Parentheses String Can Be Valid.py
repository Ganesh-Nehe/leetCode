class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the string length is odd, it can't be valid
        if len(s) % 2 != 0:
            return False

        # Check balance from left to right
        open_count = 0
        for i in range(len(s)):
            if locked[i] == '1':
                open_count += 1 if s[i] == '(' else -1
            else:
                open_count += 1  # Treat as potential '('
            if open_count < 0:
                return False  # Too many ')', even with flexible positions

        # Check balance from right to left
        close_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                close_count += 1 if s[i] == ')' else -1
            else:
                close_count += 1  # Treat as potential ')'
            if close_count < 0:
                return False  # Too many '(', even with flexible positions

        return True        