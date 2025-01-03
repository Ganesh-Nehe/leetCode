class Solution {
    public int waysToSplitArray(int[] nums) {
        int n = nums.length;
        long total = 0;
        for (int num : nums) {
            total += num; 
        }

        long lS = 0;
        int Splits = 0;

        for (int i = 0; i < n - 1; i++) { 
            lS += nums[i];
            long rS = total - lS;

            if (lS >= rS) {
                Splits++;
            }
        }

        return Splits;
    }
}