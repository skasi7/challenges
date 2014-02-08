import re

pan_re = re.compile('[A-Z]{5}[0-9]{4}[A-Z]')
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        pan = raw_input().strip()
        print 'NO' if pan_re.match(pan) is None else 'YES'

