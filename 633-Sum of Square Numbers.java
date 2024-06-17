class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            long b2 = c - a * a;
            long sqrtB = (long) Math.sqrt(b2);
            if (sqrtB * sqrtB == b2) {
                return true;
            }
        }
        return false;
    }
}