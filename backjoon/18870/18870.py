import sys
from collections import defaultdict


def main():
    N = int(sys.stdin.readline())
    input_list = [0] + list(map(int, sys.stdin.readline().split()))

    # input과 output을 뒤집음
    dic = defaultdict(list)

    for idx, element in enumerate(input_list[1:], 1):
        # print(f"idx = {idx}, element = {element}")
        dic[element].append(idx)

    min_key_nums = [-1]
    cnt = 0
    sorted_keys = sorted(dic.keys())
    for idx, element in enumerate(input_list[1:], 1):
        for key in sorted_keys:
            # print(f"key = {key}")
            if key < element:
                cnt += 1
            else:
                break

        min_key_nums.append(cnt)
        cnt = 0

    print(*min_key_nums[1:])


main()
