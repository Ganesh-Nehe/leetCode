class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        a_s = [0] * (n + 1)

        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            a_s[start] += delta
            a_s[end + 1] -= delta
        c_s = 0
        result = []
        for i in range(n):
            c_s += a_s[i]

            net_shift = c_s % 26

            new_char = chr((ord(s[i]) - ord('a') + net_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)