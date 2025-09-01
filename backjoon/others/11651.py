import sys

n = int(sys.stdin.readline())
dots=[]

for i in range(n):
    dots.append(list(map(int,sys.stdin.readline().split())))

dots.sort(key=lambda x: (x[1],x[0]))

for dot in dots:
    print(dot[0], dot[1])
