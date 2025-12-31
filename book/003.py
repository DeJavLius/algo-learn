# 11659
# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
#
# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.
#
# 제한
# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 100,000
# 1 ≤ i ≤ j ≤ N
import sys

if __name__ == '__main__':
    (count, lines) = (sys.stdin.readline().split(" "))
    na = sys.stdin.readline().split(" ")
    nas = [0 for a in range(int(count))]
    result = [0 for a in range(int(lines))]

    for (i, num) in enumerate(na):
        if i != 0:
            nas[i] = nas[i-1] + int(num)
        else:
            nas[i] = int(num)

    for i in range(int(lines)):
        (si, ei) = (sys.stdin.readline().split(" "))
        (si, ei) = (int(si) - 1, int(ei) - 1)

        result[i] = nas[ei] - nas[(si - 1 if si > 0 else 0)] + (nas[si] if si == 0 else 0)

    for r in result:
        sys.stdout.write(str(r) + "\n")