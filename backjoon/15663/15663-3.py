import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    used = [False] * n

    def solve(seq):
        if len(seq) == m:
            print(*seq)
            return

        prev = 0
        for i in range(n):
            if used[i] or nums[i] == prev:
                continue
            used[i] = True
            solve(seq + [nums[i]])
            used[i] = False
            prev = nums[i]

    solve([])


main()
