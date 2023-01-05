# DFS TEST
import sys
from collections import deque
input= sys.stdin.readline
graph_list = {1: set([2, 3]),
              2: set([1, 3, 4, 5]),
              3: set([1, 2, 6, 7]),
              4: set([2, 5]),
              5: set([2, 4]),
              6: set([3, 7]),
              7: set([3, 6])
}

root_node = 1

visited = []
def DFS_with_adj_list(graph_list, root):
    visited.append(root)
    for node in graph_list[root]:
        if node not in visited:
            DFS_with_adj_list(graph_list, node)
    return visited

print(DFS_with_adj_list(graph_list, root_node))