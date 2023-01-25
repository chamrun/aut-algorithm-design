from copy import deepcopy


def main():
    graph, num_vertices = get_input_graph()
    maximum_useless_weight = find_maximum_useless_weight(graph, num_vertices)
    print(maximum_useless_weight)


def find_maximum_useless_weight(graph, num_vertices):
    maximum_useless_weight = 0
    for _, _, weight in graph:
        maximum_useless_weight += weight

    index = 0
    counter = 0

    parent = [i for i in range(num_vertices)]
    rank = [0 for _ in range(num_vertices)]
    mst = []
    while counter < num_vertices - 1:

        last_edge = deepcopy(graph[index])
        index = index + 1
        u_root = find_root(parent, last_edge[0])
        v_root = find_root(parent, last_edge[1])

        if u_root != v_root:
            maximum_useless_weight -= last_edge[2]
            counter = counter + 1

            merge_components(parent, rank, u_root, v_root)
            mst.append(last_edge)



    return maximum_useless_weight


def merge_components(parent, rank, u_root, v_root):
    u_root_root = find_root(parent, u_root)
    v_root_root = find_root(parent, v_root)

    if rank[u_root_root] < rank[v_root_root]:
        parent[u_root_root] = v_root_root

    elif rank[u_root_root] > rank[v_root_root]:
        parent[v_root_root] = u_root_root

    else:
        rank[u_root_root] += 1
        parent[v_root_root] = u_root_root


def find_root(parent, i):

    if parent[i] == i:
        return i

    return find_root(parent, parent[i])


def get_input_graph():
    num_vertices, num_edges = [int(x) for x in input().split()]
    graph = []

    for _ in range(num_edges):
        vertex1, vertex2, weight = [int(x) for x in input().split()]
        graph.append([vertex1, vertex2, int(weight)])

    graph = sorted(graph, key=lambda item: item[2])
    return graph, num_vertices


if __name__ == '__main__':
    main()
