import sys
from collections import defaultdict


def main():
    N, r, c = map(int, input().split())

    multi_num = defaultdict(int)

    length = 2**N

    low = 0
    high = length - 1
    mid = (low + high) // 2

    low_r, low_c = low, low
    high_r, high_c = high, high
    mid_r, mid_c = mid, mid

    cur = N

    while low_r < high_r and low_c < high_c:
        if low_r <= r <= mid_r and low_c <= c <= mid_c:
            multi_num[cur] = 0

            high_r = mid_r
            high_c = mid_c

            # print("0곱")

        elif low_r <= r <= mid_r and mid_c < c <= high_c:
            multi_num[cur] = 1

            high_r = mid_r
            low_c = mid_c + 1

            # print("1곱")

        elif mid_r < r <= high_r and mid_c < c <= high_c:
            multi_num[cur] = 3

            low_r = mid_r + 1
            low_c = mid_c + 1

            # print("3곱")

        elif mid_r < r <= high_r and low_c <= c <= mid_c:
            multi_num[cur] = 2

            low_r = mid_r + 1
            high_c = mid_c

            # print("2곱")

        else:
            print("이상함")

        mid_r = (low_r + high_r) // 2
        mid_c = (low_c + high_c) // 2

        cur -= 1

    result_sum = multi_num[1]
    for i in range(2, N + 1):
        result_sum += (4 ** (i - 1)) * multi_num[i]

    print(result_sum)


main()
