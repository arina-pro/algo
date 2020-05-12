import numpy as np


def delete_loops_and_multi_links(graph):
    graph_list = list(graph)
    L = len(graph_list)
    aux = np.empty(L)
    for i in range(L):
        for j in reversed(range(len(graph[i]))):
            if graph[i][j] == i:
                graph_list[i].pop(j)
            elif aux[graph[i][j]] == i:
                graph_list[i].pop(j)
            else:
                aux[graph[i][j]] = i
    return np.array(graph_list)


if __name__ == "__main__":
    multi1 = np.array([[0, 1, 2], [4, 2, 3, 3, 2, 4], [], [], [4]])
    print(delete_loops_and_multi_links(multi1))