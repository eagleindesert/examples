import sys
from collections import deque


def main():
    N, K = map(int, sys.stdin.readline().split())

    # graph
    # it only describes index of nodes.
    # if you want to know connected nodes list from a index: 1 's node
    # use graph[1].
    graph = []

    # index starts from 0
    # if you want to search idx: 3 's value,
    # use key_value_list[3].
    graph_kv_list = []
    graph_kv_list.append(N)

    count = 0
    idx_target = 0
    while True:
        graph_kv_list.insert(3 * count + 1, graph_kv_list[count] - 1)
        graph_kv_list.insert(3 * count + 2, graph_kv_list[count] + 1)
        graph_kv_list.insert(3 * count + 3, graph_kv_list[count] * 2)

        if (
            graph_kv_list[3 * count + 1] == K
            or graph_kv_list[3 * count + 2] == K
            or graph_kv_list[3 * count + 3] == K
        ):
            idx_target = 3 * count + 1
            break

        count += 1

    depth = 0
    if N != K:
        while idx_target > 0:
            idx_target = (idx_target - 1) // 3
            depth += 1

    print(depth)


main()
