class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums) 
        operations = 0
        
        while nums[0] < k:
            x = heappop(nums) 
            y = heappop(nums) 
            new_value = min(x, y) * 2 + max(x, y)    
            heappush(nums, new_value)  
            operations += 1  
        
        return operations