import sys
sys.set_int_max_str_digits(10000)
n = int(sys.stdin.readline())
counter, x, y = 0, 0, 0
for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    if r > y:
        if l <= y:
            y = r
        else:
            counter += y - x
            x, y = l, r
counter += y - x
sys.stdout.write(str(counter) + '\n')