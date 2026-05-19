
def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root) 
        for neighbour in graph[root]: 
            dfs(visited, graph, neighbour) #recursive approach

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

visited = set() 

dfs(visited, graph, 'A')





#BFS 

def bfs(graph, start):
    visited = []        # List to keep track of visited nodes
    queue = [start]     # Queue to hold nodes to visit next

    while queue:
        node = queue.pop(0)   # Remove the first element from the queue

        if node not in visited:
            print(node)       # Visit the node (print it)
            visited.append(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS traversal starting from node A:")
bfs(graph, 'A')
