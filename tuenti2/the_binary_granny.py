#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# Special thanks to safull by the tips

import sys

def dec2bin(n):
  if n == 0:
    return ''

  digits = []
  while n > 1:
    digits += str(n % 2)
    n /= 2
  digits += str(n)

  digits.reverse()
  return ''.join(digits)

def compute(line):
  n = int(line)
  if n == 0:
    return 0

  line = dec2bin(n)[1:]

  ones = 1
  total = 0
  for c in line:
    if c == '0':
      # Compute
      total += 2 * ones - 1
      ones = 1
    else:
      ones += 1

  total += ones
  return total

def main():
  lines = (line for line in sys.stdin)
  cases = int(lines.next())
  for testcase in xrange(cases):
    case = lines.next()
    print 'Case #%d: %d' % (testcase + 1, compute(case[:-1]))

if __name__ == '__main__':
  main()

