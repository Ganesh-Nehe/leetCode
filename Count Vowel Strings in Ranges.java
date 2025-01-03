class Solution {
    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }

    public int[] vowelStrings(String[] words, int[][] queries) {
        int n = words.length;
        int[] prefix = new int[n + 1];
        int[] result = new int[queries.length];

        for (int i = 0; i < n; i++) {
            String word = words[i];
            if (isVowel(word.charAt(0)) && isVowel(word.charAt(word.length() - 1))) {
                prefix[i + 1] = prefix[i] + 1;
            } else {
                prefix[i + 1] = prefix[i];
            }
        }

        for (int i = 0; i < queries.length; i++) {
            int li = queries[i][0];
            int ri = queries[i][1];
            result[i] = prefix[ri + 1] - prefix[li];
        }

        return result;
    }
}
