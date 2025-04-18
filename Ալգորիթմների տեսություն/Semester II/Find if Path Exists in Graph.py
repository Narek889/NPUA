def find(edges, n, source, destination, visited=None):
    if visited is None:
        visited = set()

    graph = {i: [] for i in range(n)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    if source not in visited:
        print(source)
        visited.add(source)
        for neighbor in graph[source]:
            if neighbor == destination:
                return True
            if find(edges, n, neighbor, destination, visited):
                return True
    return False


edges = [[0, 1], [1, 2], [2, 0]]
n = 3
destination = 2
source = 0
print(f"ex 1 = {find(edges, n, source, destination)}")


edges_2 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
n_2 = 6
destination_2 = 5
source_2 = 0
print(f"ex 2 = {find(edges_2, n_2, source_2, destination_2)}")
