import heapq  # Used for priority queue operations (open set)

# Define a Node class to represent each cell in the grid
class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (row, col) of the current cell
        self.parent = parent      # The node from which this node was reached
        self.g = g                # Cost from start to this node
        self.h = h                # Estimated cost from this node to goal (heuristic)
        self.f = g + h            # Total cost = g + h

    def __lt__(self, other):
        # Allows comparison between Node objects based on f value for heapq
        return self.f < other.f

# Heuristic function: Manhattan distance between two points
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search function to find the shortest path in a grid
def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])  # Get the size of the grid
    
    open_set = []         # Priority queue for nodes to be explored
    closed_set = set()    # Set of already visited positions

    # Create the start node and add it to the open set
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        # Pop the node with the lowest f value
        current_node = heapq.heappop(open_set)

        # If goal is reached, reconstruct the path
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)  # Add each node to the path
                current_node = current_node.parent  # Move to the parent
            return path[::-1]  # Reverse the path to start from the beginning

        # Mark the current position as visited
        closed_set.add(current_node.position)

        # Explore the 4 possible directions: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)

            # Check if the neighbor is within grid bounds
            if (0 <= neighbor_pos[0] < rows and
                0 <= neighbor_pos[1] < cols and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and  # Not an obstacle
                neighbor_pos not in closed_set):                # Not already visited

                g_cost = current_node.g + 1  # Cost from start to neighbor
                h_cost = heuristic(neighbor_pos, goal)  # Heuristic from neighbor to goal
                neighbor_node = Node(neighbor_pos, current_node, g_cost, h_cost)

                # Add neighbor to the open set (priority queue)
                heapq.heappush(open_set, neighbor_node)

    return None  # If no path is found

# Example usage
grid = [
    [0, 1, 0, 0, 0],  # 0 = walkable, 1 = obstacle
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Starting cell (top-left corner)
goal = (4, 4)   # Target cell (bottom-right corner)

# Call the A* function
path = a_star_search(grid, start, goal)

# Print the result
print("Shortest Path:", path)
