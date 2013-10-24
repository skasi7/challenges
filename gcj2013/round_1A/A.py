#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def challenge():
  r, t = map(int, getline().split())

  n = int((-(2 * r - 1) + ((2 * r - 1) ** 2 + 8 * t) ** .5) / 4)
  while 2 * n * r + n * (2 + 4 * (n - 1)) / 2 > t:
    n -= 1
  print n

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

