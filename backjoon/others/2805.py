"""
import sys
import bisect


def main():
    N, M = map(int, sys.stdin.readline().split())
    tree_list = list(map(int, sys.stdin.readline().split()))
    tree_list.sort()

    sum_list = total_sum(tree_list)

    print(type(sum_list))

    # H는 0과 H_max 사이의 값 리스트(가상)에 존재
    H_max = max(tree_list)
    low = 0
    high = H_max
    H = (low + high) // 2

    while low < high:
        idx = find_index(tree_list, H)
        cut_sum = range_sum(sum_list, idx, len(sum_list) - 1)
        if cut_sum > M:
            low = H
            H = (low + high) // 2
        elif cut_sum < M:
            high = H
            H = (low + high) // 2
        else:
            print(H)
            break


# def cut_everything(H, tree_list):
#    sum = 0
#    for tree in tree_list:
#        if tree <= H:
#            continue
#        sum = sum + tree - H
#    return sum
#


def find_index(arr, value):
    idx = bisect.bisect_right(arr, value)
    return idx


def range_sum(sum_list, k, n):
    if k == 0:
        return sum_list[n]
    return sum_list[n] - sum_list[k - 1]


def total_sum(input_list):
    sum_list = [input_list[0]]
    for i in range(1, len(input_list)):
        sum_list.append(sum_list[i - 1] + input_list[i])
    return sum_list


# print(cut_everything(3, [1,2,3,4,5,6]))

main()
"""

###########################################

import sys


def calculate_wood(tree_list, H):
    """높이 H로 잘랐을 때 얻는 나무 길이 계산"""
    total = 0
    for tree in tree_list:
        if tree > H:
            total += tree - H
    return total


def main():
    N, M = map(int, sys.stdin.readline().split())
    tree_list = list(map(int, sys.stdin.readline().split()))

    # H의 범위: 0 ~ 가장 큰 나무 높이
    left = 0
    right = max(tree_list)
    result = 0

    # 이분탐색
    while left <= right:
        mid = (left + right) // 2
        wood = calculate_wood(tree_list, mid)

        if wood >= M:  # 충분히 얻음 → H를 더 높일 수 있음
            result = mid
            left = mid + 1
        else:  # 부족함 → H를 낮춰야 함
            right = mid - 1

    print(result)


main()
