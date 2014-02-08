import re

number_re = re.compile('([0-9]{1,3})[ -]([0-9]{1,3})[ -]([0-9]{4,10})')
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        number = raw_input().strip()
        m = number_re.match(number)
        print 'CountryCode=%s,LocalAreaCode=%s,Number=%s' % (
            m.group(1), m.group(2), m.group(3))

