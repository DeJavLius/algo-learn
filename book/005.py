# 문제
# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
#
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.
#
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
#
# 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)
#
# 출력
# 첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
import sys

input = sys.stdin.readline

(n, m) = map(int, input().split())
ins_sum = [0]
sub_dic = {}
answers = 0

for i, v in enumerate(input().split()):
  calc = (ins_sum[i] + int(v)) % m
  ins_sum.append(calc)

  if sub_dic.get(calc):
    sub_dic[calc] += 1
  else:
    sub_dic[calc] = 1

for k, v in sub_dic.items():
  if v > 1:
    f = v * (v - 1) / 2
    answers += int(f)

  if k == 0:
    answers += v

print(answers)