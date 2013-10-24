#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import itertools
import math
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def is_palindrome(x):
  x_str = str(x)
  return x_str == x_str[::-1]

# For large1 input
my_palindromes = {x
    for x in xrange(1, 10**7)
    if is_palindrome(x) and is_palindrome(x ** 2)}

def challenge():
  A, B = map(int, getline().split());
  A_root = int(math.ceil(A**.5))
  B_root = int(math.floor(B**.5))

  print len([x for x in xrange(A_root, B_root + 1) if x in my_palindromes])

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

