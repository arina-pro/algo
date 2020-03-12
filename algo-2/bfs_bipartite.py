import numpy as np
import queue as q

def is_bipartite(G, s):
    """Returns 1 if graph is bipartite; otherwise 0."""
    Q = q.Queue(len(G))
    colored = np.zeros(len(G))
    colored[s] = 1
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if colored[v] == 0:
                colored[v] = -1 * colored[u]
                Q.put(v)
            elif colored[v] == colored[u]:
                return 0
    return 1

if __name__ == "__main__":
    graph = np.array([[1, 2], [2, 3, 4], [], [], []])
    graph1 = np.array([[1, 2], [3, 4], [], [], []])
    print(is_bipartite(graph, 0))
    print(is_bipartite(graph1, 0))
