import sys

def main():
    N = int(sys.stdin.readline())
    coords = list(map(int, sys.stdin.readline().split()))

    unique_list = set(coords)
    sorted_unique = sorted(unique_list)

    rank = {val: idx for idx, val in enumerate(sorted_unique)}

    result = [rank[x] for x in coords]

    print(*result)

main()