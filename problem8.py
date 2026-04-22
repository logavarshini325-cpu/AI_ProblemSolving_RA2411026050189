

from collections import deque   # IMPORTANT FIX

# Graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS Algorithm
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return "No path found"

# DFS Algorithm
def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return "No path found"

# Input
start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

# Output
print("\nBFS Path:", bfs(graph, start, goal))
print("DFS Path:", dfs(graph, start, goal))
