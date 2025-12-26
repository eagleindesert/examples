import sys
import bisect


def main():
    N, M = map(int, sys.stdin.readline().split())
    tree_list = list(map(int, sys.stdin.readline().split()))

    tree_list.sort()

    max_H = tree_list[len(tree_list) - 2]

    for i in range(max_H, -1, -1):
        k = bisect.bisect_right(tree_list, i)
        print(f"k is {k}")

        sum = range_sum(tree_list, k, len(tree_list) - 1)
        rest = sum - ((len(tree_list) - 1) - k + 1) * i
        #print(rest)

        if rest >= M:
            print(i)
            break
    
    
# def find_index(arr, value):
#    idx = bisect.bisect_right(arr, value)
#

# k부터 n까지의 합
def range_sum(input_list, k, n):
    sum_list = total_sum(input_list)

    if k == 0:
        return sum_list[n]

    return sum_list[n] - sum_list[k - 1]


def total_sum(input_list):
    sum_list = [input_list[0]]
    for i in range(1, len(input_list)):
        sum_list.append(sum_list[i - 1] + input_list[i])
    return sum_list


main()
