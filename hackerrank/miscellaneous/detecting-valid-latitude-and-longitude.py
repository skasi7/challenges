import re

number_re_str = r'[-+]?[1-9][0-9]*(\.[0-9]+)?'
lat_long_re = re.compile(r'\((%s), (%s)\)' % (number_re_str, number_re_str))
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        line = raw_input().strip()
        m = lat_long_re.match(line)
        print 'Valid' if m is not None and \
                -90 <= float(m.group(1)) <= 90 and \
                -180 <= float(m.group(3)) <= 180 else \
                'Invalid'

