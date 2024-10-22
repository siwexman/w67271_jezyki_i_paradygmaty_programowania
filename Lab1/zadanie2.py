from collections import deque

def bfs_task(graph, start, end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end: return path

        if node not in visited:
            for neighbour in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)

    return None

graph = {
    'A': ['B', 'C']
}