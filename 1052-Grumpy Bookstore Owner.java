class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int n = customers.length;
        int totalSatisfied = 0;
        for (int i = 0; i < n; i++) {
            if (grumpy[i] == 0) {
                totalSatisfied += customers[i];
            }
        }
        int maxAdditional = 0;
        int currentAdditional = 0;
        for (int i = 0; i < minutes; i++) {
            if (grumpy[i] == 1) {
                currentAdditional += customers[i];
            }
        }
        maxAdditional = currentAdditional;
        for (int i = minutes; i < n; i++) {
            if (grumpy[i] == 1) {
                currentAdditional += customers[i];
            }
            if (grumpy[i - minutes] == 1) {
                currentAdditional -= customers[i - minutes];
            }
            maxAdditional = Math.max(maxAdditional, currentAdditional);
        }  
        return totalSatisfied + maxAdditional;
    }
}
