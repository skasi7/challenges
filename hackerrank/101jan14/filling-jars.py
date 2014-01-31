def challenge(n, operations):
    total = 0
    for a, b, k in operations:
        total += (b - a + 1) * k
    return total / n

if __name__ == '__main__':
    n, m = map(int, raw_input().strip().split())
    operations = list()
    for _ in xrange(m):
        operations.append(map(int, raw_input().strip().split()))
    print challenge(n, operations)

