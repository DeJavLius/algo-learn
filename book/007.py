n = int(input())
m = int(input())
mat = sorted([int(a) for a in input().split()])

count = 0
si = 0
ei = 1
size = len(mat) - 1
sum = 0

while si < size - 1:
  if ei == size:
    si += 1
    ei = si + 1
  else:
    ei += 1

  sum = mat[si] + mat[ei]

  if sum == m:
    count += 1
  else:
    sum -= mat[ei]

print(count)