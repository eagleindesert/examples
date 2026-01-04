from collections import deque


def main():
    N, K = map(int, input().split())

    if N == K:
        print(0)
        return

    # visited[i] = i 위치까지 가는데 걸린 시간
    visited = [-1] * 100001
    visited[N] = 0

    queue = deque([N])

    while queue:
        current = queue.popleft()

        # 다음 위치들
        next_positions = [current - 1, current + 1, current * 2]

        for next_pos in next_positions:
            # 범위 체크 및 방문 체크
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

            if next_pos == K:
                print(visited[K])
                return


main()
