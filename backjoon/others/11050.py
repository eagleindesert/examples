import sys

def main():
    top = 1
    bot = 1

    N, K = map(int, sys.stdin.readline().split())

    for i in range(N, N-K, -1):
        top *= i

    for i in range(2, K+1):
        bot *= i

    print(top // bot)
        
main()