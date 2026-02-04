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

    # 우선 노드 1부터 DFS
    # 스택 저장 양식은 다음과 가다
    # stack = [[(K, W), D], [...], ...]
    # K는 노드 이름, W는 그 노드의 가중치, D는 그 노드의 깊이
    stack = []

    # 방문했을 시 1, 방문 X는 0
    visited = [0] * (n + 1)

    # 최대 깊이 고려
    # 깊이는 0부터 시작
    weight_list = [0] * 10000

    # weight의 최댓값
    max_weight = -1

    # 경유 노드
    dest_node = -1

    stack.append([(1, 0), 0])

    while stack:
        bundle = stack.pop()
        cur = bundle[0][0]

        if visited[cur] == 0:
            visited[cur] = 1

            ## bundle[1] = D
            ## bundle[0][1] = W
            weight_list[bundle[1]] = bundle[0][1]
            #print(f"Key = {bundle[0][0]}, Depth={bundle[1]}")

            ## 방문하지 않는 점 중에서 None일 때!
            ## 양방향 그래프라 flag 변수를 설정
            is_there = 0
            for line in graph[cur]:
                if visited[line[0]] == 0:
                    is_there = 1
                    break

            # 리프 노드인 경우
            if is_there == 0:
                if sum(weight_list[: bundle[1] + 1]) > max_weight:
                    max_weight = sum(weight_list[: bundle[1] + 1])
                    dest_node = cur

            else:
                for K, W in reversed(graph[cur]):
                    if visited[K] == 0:
                        stack.append([(K, W), bundle[1] + 1])

            is_there = 0

    ################ 두번째 순회
    #print(max_weight)
    #print("###########################")

    visited = [0] * (n + 1)
    weight_list = [0] * 10000
    max_weight = -1
    stack.append([(dest_node, 0), 0])

    while stack:
        bundle = stack.pop()
        cur = bundle[0][0]

        if visited[cur] == 0:
            visited[cur] = 1

            ## bundle[1] = D
            ## bundle[0][1] = W
            weight_list[bundle[1]] = bundle[0][1]
            #print(f"Key = {bundle[0][0]}, Depth={bundle[1]}")

            ## 방문하지 않는 점 중에서 None일 때!
            ## 양방향 그래프라 flag 변수를 설정
            is_there = 0
            for line in graph[cur]:
                if visited[line[0]] == 0:
                    is_there = 1
                    break

            if is_there == 0:
                if sum(weight_list[: bundle[1] + 1]) > max_weight:
                    max_weight = sum(weight_list[: bundle[1] + 1])
                    dest_node = cur

            else:
                for K, W in reversed(graph[cur]):
                    if visited[K] == 0:
                        stack.append([(K, W), bundle[1] + 1])

            is_there = 0

    print(max_weight)


main()
