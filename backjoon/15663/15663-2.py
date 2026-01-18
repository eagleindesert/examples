import sys

input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    input_list = sorted(map(int, input().split()))
    branch_list = input_list.copy()
    visited = [False] * N
    selected = []

    def dfs(selected):
        if len(selected) == M:
            print(*selected)
            return

        # 같은 깊이의 분기 중, 중복이 없게 하기 위해 prev 사용
        prev = -1
        for idx, value in enumerate(branch_list):
            if visited[idx] == False and value != prev:

                visited[idx] = True
                selected.append(value)
                # print(f"방문 = {node}")

                dfs(selected)

                visited[idx] = False
                selected.pop()

                prev = value

    dfs(selected)


main()
