class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0]
        for i in range(n - 1):
            original.append(original[-1] ^ derived[i])
        if original[-1] ^ original[0] == derived[-1]:
            return True
        original = [1]
        for i in range(n - 1):
            original.append(original[-1] ^ derived[i])
        if original[-1] ^ original[0] == derived[-1]:
            return True
        return False
