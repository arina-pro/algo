import numpy as np
import queue as q

def is_bipartite(G, s=0):
    """Returns 1 if graph is bipartite; otherwise 0."""
    Q = q.Queue(len(G))
    colored = np.zeros(len(G), dtype=int)
    while True:
        colored[s] = 1
        Q.put(s)
        while True:
            u = Q.get()
            for v in G[u]:
                if colored[v] == 0:
                    colored[v] = -1 * colored[u]
                    Q.put(v)
                elif colored[v] == colored[u]:
                    return 0
            if Q.empty():
                break
        if np.prod(colored) != 0:
            break
        for ind, c in enumerate(colored):
            if c == 0:
                s = ind
                print("found", s)
                break
    return 1

if __name__ == "__main__":
    graph = np.array([[1, 2], [2, 3, 4], [], [], []])
    graph1 = np.array([[1, 2], [3, 4], [], [], [], [6], [7], [5]])
    graph2 = np.array([[1, 2], [3, 4], [], [], [], [6], [], []])
    print(is_bipartite(graph, 0))
    print(is_bipartite(graph1, 0))
    print(is_bipartite(graph2))
