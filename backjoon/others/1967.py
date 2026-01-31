import sys
from collections import defaultdict

input = sys.stdin.readline


def main():
    # {Node1 : [(K1, W1), (K2, W2)], Node2: : [(K1, W1)]}
    # 으로 저장됨
    graph = defaultdict(list)

    n = int(input())

    for i in range(n - 1):
        K1, K2, W = map(int, input().split())
        graph[K1].append((K2, W))
        graph[K2].append((K1, W))

    # 자식 노드 정렬은 어떻게 구현?
    # ex) 만약 graph[1] = [(3, 2), (2, 3)] 이다 라고 하면
    # 앞 원소를 기준으로 정렬하는 코드가 필요
    # 다만 이 문제에서는 불필요하긴 해~
    for key in graph:
        graph[key].sort(key=lambda x: x[0])

    print(graph)


main()
