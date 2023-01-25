import heapq


def shortest_paths(graph, start, end):
    # Initialize the heap and distances dictionary
    heap = [(0, start)]
    dist = {start: 0}
    paths = {start: [start]}
    # While the heap is not empty
    while heap:
        # Extract the node with the smallest distance
        (d, node) = heapq.heappop(heap)
        # If we have reached the end node, return the paths and distance
        if node == end:
            return (dist[node], paths[node])
        # If we have already visited this node, continue
        if d > dist.get(node, float('inf')):
            continue
        # Update the distance of all adjacent nodes
        for neighbor in graph[node]:
            new_dist = d + graph[node][neighbor]
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
                paths[neighbor] = paths[node] + [neighbor]
    # If we have not found any path, return None
    return None


if __name__ == '__main__':
    # Example usage

    num_vertices, num_edges = [int(x) for x in input().split()]

    edges = []
    graph = {}

    for _ in range(num_edges):
        vertex1, vertex2, weight = [int(x) for x in input().split()]
        if vertex1 not in graph:
            graph[vertex1] = {}

        graph[vertex1][vertex2] = weight

        if vertex2 not in graph:
            graph[vertex2] = {}

        graph[vertex2][vertex1] = weight
        # edges.append(Edge(vertex1, vertex2, weight))

    # graph = {'A': {'B': 1, 'C': 4},
    #          'B': {'A': 1, 'C': 2, 'D': 5},
    #          'C': {'A': 4, 'B': 2, 'D': 1},
    #          'D': {'B': 5, 'C': 1}}

    paths = shortest_paths(graph, 0, num_vertices - 1)
    print(paths)
