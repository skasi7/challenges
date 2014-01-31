import math

def challenge(m, n):
    # Combinations of m + n - 2 positions chosen n - 1 by n - 1
    if m < n:
        m, n = n, m
    result = 1
    for i in xrange(m, m + n - 1):
        result *= i
    return result / math.factorial(n - 1)

if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        m, n = map(int, raw_input().strip().split())
        print challenge(m, n) % (10**9 + 7)

