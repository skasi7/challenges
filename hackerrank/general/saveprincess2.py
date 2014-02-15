def displayPathtoPrincess(n, grid):
    m = p = None
    for i, row in enumerate(grid):
        if 'm' in row:
            m = (i, row.index('m'))
        if 'p' in row:
            p = (i, row.index('p'))
    di, dj = (p[0] - m[0], p[1] - m[1])
    if di != 0:
        print 'DOWN' if di > 0 else 'UP'
        return
    if dj != 0:
        print 'RIGHT' if dj > 0 else 'LEFT'
        return

if __name__ == '__main__':
    n = input()
    m = map(int, raw_input().strip().split())
    grid = []
    for i in xrange(0, n):
        grid.append(raw_input().strip())

    displayPathtoPrincess(n, grid)

