# 1253
import sys
input = sys.stdin.readline
n = int(input())
numbers = sorted(list(map(int, input().split())))
count = 0

for i, v in enumerate(numbers):
  s_i = 1 if 0 == i else 0
  e_i = n - (2 if n == i + 1 else 1)

  while s_i < e_i:
    if numbers[s_i] + numbers[e_i] == v:
      count += 1
      break
    elif numbers[s_i] + numbers[e_i] > v:
      e_i = e_i - (2 if e_i - 1 == i else 1)
    else:
      s_i = s_i + (2 if s_i + 1 == i else 1)

print(count)