import sys

countDic = {"nothing": 0, "colored": 0}


def div(board, x1, y1, x2, y2):
    mid = (x2 - x1) // 2  # (정사각형의 한 변의 길이 - 1)의 중간

    if board[y1][x1] == 1:
        colored = True

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if board[i][j] == 0:
                    colored = False
                    break
            if colored == False:
                break

        if colored == True:
            countDic["colored"] += 1
            return

    elif board[y1][x1] == 0:
        nothing = True

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                if board[i][j] == 1:
                    nothing = False
                    break
            if nothing == False:
                break

        if nothing == True:
            countDic["nothing"] += 1
            return

    div(board, x1, y1, x1 + mid, y1 + mid)
    div(board, x1 + mid + 1, y1, x2, y1 + mid)
    div(board, x1, y1 + mid + 1, x1 + mid, y2)
    div(board, x1 + mid + 1, y1 + mid + 1, x2, y2)


def main():
    board = []

    N = int(sys.stdin.readline())
    for _ in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        board.append(temp)
    # print(board)

    div(board, 0, 0, N-1, N-1)

    """ x1, y1, x2, y2 = 0, 0, 7, 7
    mid = (x2 - x1) // 2
    print(x1, y1, x1 + mid, y1 + mid)
    print(x1 + mid + 1, y1, x2, y1 + mid)
    print(x1, y1 + mid + 1, x1 + mid, y2)
    print(x1 + mid + 1, y1 + mid + 1, x2, y2) """

    print(countDic["nothing"])
    print(countDic["colored"])


main()
