#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import string
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def challenge():
  print getline()

# Main entry point
if __name__ == '__main__':
  L, D, testcases = map(int, getline().split())
  words = [getline() for _ in xrange(D)]

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

