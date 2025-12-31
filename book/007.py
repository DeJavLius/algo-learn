n = int(input())
m = int(input())
mat = sorted([int(a) for a in input().split()])

count = 0
s_idx = 0
e_idx = len(mat)-1

while s_idx < e_idx:
  if mat[s_idx] + mat[e_idx] == m:
    count += 1
    s_idx += 1
    e_idx -= 1
  elif mat[s_idx] + mat[e_idx] < m:
    s_idx += 1
  else:
    e_idx -= 1

print(count)