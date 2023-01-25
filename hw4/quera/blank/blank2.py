import queue


# Node class
class Node:

    # Stores the node
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

    # Costume comparator
    def __lt__(self, other):
        return self.cost < other.cost


# Function to insert a node in adjacency list
def addEdge(adj, x, y, w):
    adj[x].append(Node(y, w))
    adj[y].append(Node(x, w))


# Auxiliary function to find shortest paths using Dijekstra
def dijkstra(adj, src, n, dist, paths):
    # Stores the distances of every node in shortest order
    pq = queue.PriorityQueue()

    # Stores if a vertex has been visited or not
    settled = set()

    # Adds the source node with 0 distance to pq
    pq.put(Node(src, 0))

    dist[src] = 0
    paths[src] = 1

    # While pq is not empty()
    while not pq.empty():

        # Stores the top node of pq
        u = pq.get().node

        # Stores the distance of node u from s
        d = pq.get().cost

        # Pop the top element
        pq.get()

        for i in range(len(adj[u])):
            to = adj[u][i].node
            cost = adj[u][i].cost

            # If edge is marked
            if (to, u) in settled:
                continue

            # If dist[to] is greater than dist[u] + cost
            if dist[to] > dist[u] + cost:
                # Add the node to to the pq
                pq.put(Node(to, d + cost))

                # Update dist[to]
                dist[to] = dist[u] + cost

                # Update paths[to]
                paths[to] = paths[u]

            # Otherwise
            elif dist[to] == dist[u] + cost:
                paths[to] = (paths[to] + paths[u])

            # Mark the edge visited
            settled.add((to, u))


# Function to find the count of shortest path and distances from source node to every other node
def findShortestPaths(adj, s, n):
    # Stores the distances of a node from source node
    dist = [float('inf') for i in range(n + 5)]

    # Stores the count of shortest paths of a node from source node
    paths = [0 for i in range(n + 5)]

    dijkstra(adj, s, n, dist, paths)


if __name__ == '__main__':
    num_vertices, num_edges = [int(x) for x in input().split()]
    res = findShortestPaths(adj, 0, n)
