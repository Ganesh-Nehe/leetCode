class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        color = {} 
        components = [] 
        
        def bfs_check_bipartite(start):
            queue = deque([start])
            color[start] = 0 
            component = []
            
            while queue:
                node = queue.popleft()
                component.append(node)
                
                for neighbor in graph[node]:
                    if neighbor in color:
                        if color[neighbor] == color[node]:  
                            return None 
                    else:
                        color[neighbor] = 1 - color[node] 
                        queue.append(neighbor)
            
            return component
        
        for node in range(1, n + 1):
            if node not in color:
                component = bfs_check_bipartite(node)
                if component is None:
                    return -1 
                components.append(component)
        
        def bfs_max_depth(start):
            queue = deque([start])
            visited = {start}
            level = 0
            
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                level += 1
            
            return level
        
        result = 0
        for component in components:
            max_depth = 0
            for node in component:
                max_depth = max(max_depth, bfs_max_depth(node))
            result += max_depth
        
        return result