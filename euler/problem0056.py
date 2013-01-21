#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# subversion info:
# $HeadURL: https://skasi-lps.googlecode.com/svn/trunk/euler/problem0056.py $
# $Author: SkAsI.7 $
# $Id: problem0056.py 25 2011-01-20 12:12:40Z SkAsI.7 $
# $Revision: 25 $


# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import itertools
import optparse
import os
import sys
import time

# Internal imports (if any)


def digitalSum(a, b):
  return sum(map(int, str(a ** b)))

def main():
  return max((digitalSum(a, b) for a in xrange(1, 100)
    for b in xrange(1, 100)))


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

