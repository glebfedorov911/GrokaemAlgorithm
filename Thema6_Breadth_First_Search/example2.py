from collections import deque


def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        current, step = queue.popleft()

        if current == target:
            return step
        
        if current not in visited:
            visited.add(current)
            for neighbour in graph.get(current, []):
                if neighbour not in visited:
                    queue.append([neighbour, step+1])

    return -1

graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": [],
    "D": ["E", "F", "G"]
}

print("A -> F:", bfs(graph, "A", "F"))
print("A -> C:", bfs(graph, "A", "C"))
print("A -> D:", bfs(graph, "A", "D"))
print("A -> J:", bfs(graph, "A", "J"))