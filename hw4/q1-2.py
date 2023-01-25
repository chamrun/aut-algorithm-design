class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight


def main():
    num_vertices, num_edges = [int(x) for x in input().split()]

    edges = []

    for _ in range(num_edges):
        vertex1, vertex2, weight = [int(x) for x in input().split()]
        edges.append(Edge(vertex1, vertex2, weight))

if __name__ == '__main__':
    main()
