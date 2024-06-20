import java.util.Arrays;

class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int left = 1;
        int right = position[position.length - 1] - position[0];
        
        while (left < right) {
            int mid = (right - left + 1) / 2 + left;
            if (canPlaceBalls(position, m, mid)) {
                left = mid; 
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
    
    private boolean canPlaceBalls(int[] position, int m, int minForce) {
        int count = 1; 
        int lastPosition = position[0];
        
        for (int i = 1; i < position.length; i++) {
            if (position[i] - lastPosition >= minForce) {
                count++;
                lastPosition = position[i];
                if (count == m) {
                    return true;
                }
            }
        }
        
        return false;
    }
}
