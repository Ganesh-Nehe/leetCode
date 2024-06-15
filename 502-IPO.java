class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        int[][] projects = new int[n][2];
        for (int i = 0; i < n; i++) {
            projects[i][0] = capital[i];
            projects[i][1] = profits[i];
        }
        Arrays.sort(projects, Comparator.comparingInt(a -> a[0]));
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int projectIndex = 0;
        for (int i = 0; i < k; i++) {
            while (projectIndex < n && projects[projectIndex][0] <= w) {
                maxHeap.offer(projects[projectIndex][1]);
                projectIndex++;
            }

            if (maxHeap.isEmpty()) {
                break;
            }
            w += maxHeap.poll();
        }
        return w;  
    }
}