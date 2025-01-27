class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[False] * numCourses for _ in range(numCourses)]
        
        # Set direct prerequisites in the graph
        for u, v in prerequisites:
            graph[u][v] = True
        
        # Floyd-Warshall algorithm to find transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = True
        
        # Process queries
        result = []
        for u, v in queries:
            result.append(graph[u][v])
        
        return result