# 11720
import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline())
    numbers = sys.stdin.readline()

    total = 0

    for number in numbers[0:-1]:
        total += int(number)

    sys.stdout.write(str(total))