def dls(graph, node, goal, depth, path):
    path.append(node)

    if depth == 0 and node == goal:
        return path

    if depth > 0:
        for neighbor in graph.get(node, []):
            result = dls(graph, neighbor, goal, depth - 1, path.copy())
            if result:
                return result

    return None


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        result = dls(graph, start, goal, depth, [])
        if result:
            return result
    return None


# -------- USER INPUT --------
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

# -------- RUN --------
result = iddfs(graph, start, goal, max_depth)

print("Result:", result)