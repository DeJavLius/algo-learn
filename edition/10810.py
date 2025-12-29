import sys

input = sys.stdin.readline

n, m = map(int, input().split())
basket = [0 for _ in range(n + 1)]

for _ in range(m):
    i, j, k = map(int, input().split())

    for a in range(i, j + 1):
        basket[a] = k

basket.pop(0)

for p in basket:
    sys.stdout.write(str(p))
    sys.stdout.write(" ")