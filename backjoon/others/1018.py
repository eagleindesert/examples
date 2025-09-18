import sys


def main():
    # 입력 보드
    inputBoard = []

    N, M = map(int, sys.stdin.readline().split())

    # M * N 크기의 보드 입력
    for i in range(N):
        inputBoard.append(sys.stdin.readline().strip())

    min_paint_cnt = 2500
    # p1과 p2를 각 대각 꼭짓점으로
    for p1_y in range(N - 7):
        for p1_x in range(M - 7):
            # p2는 종속적
            p2_x = p1_x + 7
            p2_y = p1_y + 7

            # (p1_x, p1_y)의 시작 색
            stColor = inputBoard[p1_y][p1_x]

            # 몇 번 칠했는지
            paint_cnt = 0

            if stColor == "B":
                for i in range(p1_y, p2_y + 1):
                    if i - p1_y % 2 == 0:
                        for j in range(p1_x, p2_x + 1):
                            if j - p1_x % 2 == 0:
                                if inputBoard[i][j] == "W":
                                    paint_cnt += 1
                            elif j - p1_x % 2 == 1:
                                if inputBoard[i][j] == "B":
                                    paint_cnt += 1
                    elif i - p1_y % 2 == 1:
                        for j in range(p1_x, p2_x + 1):
                            if j - p1_x % 2 == 0:
                                if inputBoard[i][j] == "B":
                                    paint_cnt += 1
                            elif j - p1_x % 2 == 1:
                                if inputBoard[i][j] == "W":
                                    paint_cnt += 1

            elif stColor == "W":
                for i in range(p1_y, p2_y + 1):
                    if i - p1_y % 2 == 0:
                        for j in range(p1_x, p2_x + 1):
                            if j - p1_x % 2 == 0:
                                if inputBoard[i][j] == "B":
                                    paint_cnt += 1
                            elif j - p1_x % 2 == 1:
                                if inputBoard[i][j] == "W":
                                    paint_cnt += 1
                    elif i - p1_y % 2 == 1:
                        for j in range(p1_x, p2_x + 1):
                            if j - p1_x % 2 == 0:
                                if inputBoard[i][j] == "W":
                                    paint_cnt += 1
                            elif j - p1_x % 2 == 1:
                                if inputBoard[i][j] == "B":
                                    paint_cnt += 1

            if min_paint_cnt > paint_cnt:
                min_paint_cnt = paint_cnt

            paint_cnt = 0

    print(min_paint_cnt)


main()
