def displayPathtoDirt(b, grid):
    near_d = None
    near_d_distance = 0
    for i, row in enumerate(grid):
        if 'd' in row:
            d = (i, row.index('d'))
            d_distance = abs(d[0] - b[0]) + abs(d[1] - b[1])
            if near_d is None or d_distance < near_d_distance:
                near_d = d
                near_d_distance = d_distance
    if near_d is None:
        return
    if near_d_distance == 0:
        print 'CLEAN'
        return
    di, dj = (near_d[0] - b[0], near_d[1] - b[1])
    if di != 0:
        print 'DOWN' if di > 0 else 'UP'
        return
    if dj != 0:
        print 'RIGHT' if dj > 0 else 'LEFT'
        return

if __name__ == '__main__':
    b = map(int, raw_input().strip().split())
    h, w = map(int, raw_input().strip().split())
    grid = []
    for i in xrange(0, h):
        grid.append(raw_input().strip()[:w])

    displayPathtoDirt(b, grid)

