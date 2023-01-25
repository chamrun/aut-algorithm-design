from collections import defaultdict


def find(parent, i):
    if i > len(parent):
        return -1
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(graph, V):
    result = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(V):
        parent.append(node)
        rank.append(0)
    while e < V - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    return result


num_vertices, num_edges = [int(x) for x in input().split()]
edges = []
graph = []
for _ in range(num_edges):
    vertex1, vertex2, weight = [int(x) for x in input().split()]
    # edges.append(Edge(vertex1, vertex2, weight))
    graph.append([vertex1, vertex2, weight])

# graph = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
V = num_vertices

mst = kruskal(graph, V)

# print the edges of minimum spanning tree

mst_weight = 0
for u, v, weight in mst:
    print("%d - %d: %d" % (u, v, weight))
    mst_weight += weight

graph_weight = 0
for _, _, weight in graph:
    graph_weight += weight

print(graph_weight - mst_weight)
