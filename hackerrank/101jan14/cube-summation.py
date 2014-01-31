def challenge(n, operations):
    values = dict()
    for operation in operations:
        if operation[0] == 'UPDATE':
            x, y, z, w = map(int, operation[1:])
            values[(x, y, z)] = w
        else:
            x1, y1, z1, x2, y2, z2 = map(int, operation[1:])
            print sum((w for (x, y, z), w in values.iteritems()
                if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2))

if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n, m = map(int, raw_input().strip().split())
        operations = list()
        for _ in xrange(m):
            operations.append(raw_input().strip().split())
        challenge(n, operations)

