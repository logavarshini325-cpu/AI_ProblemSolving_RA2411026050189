

import heapq

# Weighted graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('D', 1)],
    'D': [('F', 3)],
    'E': [('F', 1)],
    'F': []
}

def ucs(graph, start, goal):
    queue = [(0, start, [])]  # (cost, node, path)
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path + [node], cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (cost + weight, neighbor, path + [node]))

    return "No path found", 0

# Input
start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

# Output
path, cost = ucs(graph, start, goal)

print("\nOptimal Path:", path)
print("Total Cost:", cost)
