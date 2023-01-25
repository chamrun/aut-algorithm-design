import heapq

class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __str__(self):
        return f'({self.vertex1}, {self.vertex2}, {self.weight})'


def main():
    edges, num_vertices = get_input_graph()
    shortest_paths = find_number_of_shortest_paths(edges, 0, num_vertices - 1)
    print(shortest_paths[num_vertices - 1])


def get_input_graph():
    num_vertices, num_edges = [int(x) for x in input().split()]
    edges = []

    for _ in range(num_edges):
        vertex1, vertex2, weight = [int(x) for x in input().split()]
        edges.append(Edge(vertex1, vertex2, weight))

    return edges, num_vertices


def get_neighbors(edges, node):
    neighbors = []
    for edge in edges:
        if edge.vertex1 == node:
            neighbors.append(edge.vertex2)
        if edge.vertex2 == node:
            neighbors.append(edge.vertex1)
    return neighbors


def get_edge_weight(edges, node, neighbor):
    for edge in edges:
        if (edge.vertex1 == node and edge.vertex2 == neighbor) or (edge.vertex1 == neighbor and edge.vertex2 == node):
            return edge.weight


def find_number_of_shortest_paths(edges, start, end):
    heap = [(0, start)]
    dist = {start: 0}
    paths = {start: 1}
    while heap:
        (d, node) = heapq.heappop(heap)
        if node == end:
            return paths
        if d > dist.get(node, float('inf')):
            continue
        for neighbor in get_neighbors(edges, node):
            new_dist = d + get_edge_weight(edges, node, neighbor)
            if new_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
                paths[neighbor] = paths[node]
            elif new_dist == dist.get(neighbor, float('inf')):
                paths[neighbor] += paths[node]
    return None


if __name__ == '__main__':
    main()
