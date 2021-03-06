#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# subversion info:
# $HeadURL: https://skasi-lps.googlecode.com/svn/trunk/euler/problem0120.py $
# $Author: SkAsI.7 $
# $Id: problem0120.py 28 2011-01-24 16:29:27Z SkAsI.7 $
# $Revision: 28 $


# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import itertools
import optparse
import os
import sys
import time

# Internal imports (if any)


def max_func(a):
  m, b, c, a2 = 0, a - 1, a + 1, a * a
  while (b, c) != (1, 1):
    n = (b + c) % a2
    if n > m:
      m = n
    b *= a - 1
    b %= a2
    c *= a + 1
    c %= a2
  return m

def main():
  return sum(map(max_func, range(3, 1001)))


# Main entry point
if __name__ == '__main__':
  parser = optparse.OptionParser(usage="uso: %prog [options]")
  (options, args) = parser.parse_args()

  problem_file = sys.argv[0].replace('.py', '.txt')
  if os.path.exists(problem_file):
    print 'Problem: %s' % open(problem_file).read()

  t1 = time.time()
  
  print 'Solution:', main()

  lapse = time.time() - t1
  for unit in ('s'
      , 'ms'
      , 'us'
      , 'ns'):
    if lapse > 1 or unit == 'ns':
      lapse = '%.3f %s' % (lapse
          , unit)
      break
    lapse *= 1000
  print 'Time: %s' % lapse

