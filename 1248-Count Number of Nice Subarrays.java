class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int[] binary = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            binary[i] = nums[i] % 2;
        }
        
        int countOnes = 0;
        int result = 0;
        int[] prefixCount = new int[nums.length + 1];
        prefixCount[0] = 1;
        
        for (int i = 0; i < nums.length; i++) {
            countOnes += binary[i];
            if (countOnes >= k) {
                result += prefixCount[countOnes - k];
            }
            prefixCount[countOnes]++;
        }
        
        return result;
    }
}
