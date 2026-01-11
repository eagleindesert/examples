import sys


def main():
    N, M = map(int, sys.stdin.readline().split())

    input_list = list(map(int, sys.stdin.readline().split()))
    input_list.sort()

    dfs(N, M, [], set(), input_list)


def dfs(N, M, selected, included, input_list):
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(N):
        if input_list[i] in included:
            continue

        included.add(input_list[i])
        selected.append(input_list[i])

        dfs(N, M, selected, included, input_list)

        included.discard(selected.pop())


main()
