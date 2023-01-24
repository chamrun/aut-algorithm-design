class Vertex:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight

    def __str__(self):
        return f'({self.vertex1}, {self.vertex2}, {self.weight})'


def main():
    vertices = get_input_graph()
    print(vertices)


def get_input_graph():
    _, number_of_edges = [int(x) for x in input().split()]
    vertices = []

    for _ in range(number_of_edges):
        vertex1, vertex2, weight = [int(x) for x in input().split()]
        vertices.append(Vertex(vertex1, vertex2, weight))

    return vertices


if __name__ == '__main__':
    main()
