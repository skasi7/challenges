def displayPathtoPrincess(n, grid):
    m = p = None
    for i, row in enumerate(grid):
        if 'm' in row:
            m = (i, row.index('m'))
        if 'p' in row:
            p = (i, row.index('p'))
    di, dj = (p[0] - m[0], p[1] - m[1])
    if di != 0:
        print '\n'.join(['DOWN' if di > 0 else 'UP'] *
                (di if di > 0 else -di))
    if dj != 0:
        print '\n'.join(['RIGHT' if dj > 0 else 'LEFT'] *
                (dj if dj > 0 else -dj))

if __name__ == '__main__':
    n = input()
    grid = []
    for i in xrange(0, n):
        grid.append(raw_input().strip())

    displayPathtoPrincess(n, grid)

