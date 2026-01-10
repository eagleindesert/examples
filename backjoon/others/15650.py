import sys


def main():
    N, M = map(int, sys.stdin.readline().split())

    # 스택: (현재 선택한 수열, 다음에 시작할 숫자)
    stk = [([], 1)]

    while stk:
        selected, start = stk.pop()

        # M개를 모두 선택했으면 출력
        if len(selected) == M:
            print(" ".join(map(str, selected)))
            continue

        # 역순으로 스택에 넣어야 사전순 출력됨
        # for num in range(start, N + 1, 1):
        for num in range(N, start - 1, -1):
            stk.append((selected + [num], num + 1))


main()
