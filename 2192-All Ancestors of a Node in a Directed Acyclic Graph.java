class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        
        // Build the adjacency list representation of the graph
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            graph.get(to).add(from); // Reverse the edge direction for ancestor finding
        }
        
        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            answer.add(new ArrayList<>());
            boolean[] visited = new boolean[n];
            Set<Integer> ancestors = new HashSet<>();
            dfs(i, graph, visited, ancestors);
            List<Integer> ancestorList = new ArrayList<>(ancestors);
            Collections.sort(ancestorList);
            answer.set(i, ancestorList);
        }
        
        return answer;
    }
    
    private void dfs(int node, List<List<Integer>> graph, boolean[] visited, Set<Integer> ancestors) {
        if (visited[node]) return;
        
        visited[node] = true;
        
        for (int parent : graph.get(node)) {
            ancestors.add(parent);
            dfs(parent, graph, visited, ancestors);
        }
    }
}