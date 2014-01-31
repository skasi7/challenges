from fractions import gcd

def challenge(x1, y1, x2, y2):
    return gcd(abs(x2 - x1), abs(y2 - y1)) - 1

if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        x1, y1, x2, y2 = map(int, raw_input().strip().split())
        print challenge(x1, y1, x2, y2)

