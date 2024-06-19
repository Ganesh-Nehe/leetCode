class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int n = bloomDay.length;
        if (m * k > n) {
            return -1; 
        }
        
        int low = 1;
        int high = (int) 1e9; 
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canMakeBouquets(bloomDay, m, k, mid)) {
                high = mid - 1; 
            } else {
                low = mid + 1; 
            }
        }
        
        return low > (int) 1e9 ? -1 : low;
    }
    
    private boolean canMakeBouquets(int[] bloomDay, int m, int k, int days) {
        int bouquets = 0;
        int count = 0;
        
        for (int i = 0; i < bloomDay.length; i++) {
            if (bloomDay[i] <= days) {
                count++;
                if (count == k) {
                    bouquets++;
                    count = 0;
                }
            } else {
                count = 0;
            }
        }
        
        return bouquets >= m;
    }
}

