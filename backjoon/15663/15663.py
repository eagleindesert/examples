# 15663-2에서 함수 재귀 호출 이용해 풀기
import sys


def main():
    N, M = map(int, sys.stdin.readline().split())

    input_list = list(map(int, sys.stdin.readline().split()))

    input_list.sort()

    dfs(M, input_list)


# input_list가 정렬되있음
def dfs(M, input_list):
    # 스택에 [value, selected, not_visited] 형태로 저장
    stack = []

    for start in sorted(set(input_list)):
        not_visited = input_list.copy()
        not_visited.remove(start)
        stack.append([start, [start], not_visited])

        while stack:
            value, selected, not_visited = stack.pop()

            if len(selected) == M:
                print(" ".join(map(str, selected)))
                continue

            for neighbor in reversed(sorted(set(not_visited))):
                new_not_visited = not_visited.copy()
                new_not_visited.remove(neighbor)
                stack.append([neighbor, selected + [neighbor], new_not_visited])


main()
