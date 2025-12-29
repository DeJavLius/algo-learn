n = int(input())
count, si, ei, result = 1, 1, 1, 1

while ei < n:
  if result == n:
    count += 1

  if result > n:
    result -= si
    si += 1
  else:
    ei += 1
    result += ei

print(count)