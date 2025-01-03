class Solution {
    public int maxScore(String s) {
        int mScore = 0;
        int n = s.length();

        int total = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') {
                total++;
            }
        }

        int lZeros = 0;  
        int rOnes = total; 

        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == '0') {
                lZeros++;
            } else {
                rOnes--;
            }

            int score = lZeros + rOnes;
            mScore = Math.max(mScore, score);
        }

        return mScore;
    }
}