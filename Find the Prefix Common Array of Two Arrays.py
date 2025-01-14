class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_in_A = set()
        seen_in_B = set()
        result = []
        common_count = 0
        for i in range(n):
            if A[i] in seen_in_B:
                common_count += 1
            seen_in_A.add(A[i])            
            if B[i] in seen_in_A:
                common_count += 1
            seen_in_B.add(B[i])            
            result.append(common_count)        
        return result