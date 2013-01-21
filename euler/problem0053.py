#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# subversion info:
# $HeadURL: https://skasi-lps.googlecode.com/svn/trunk/euler/problem0053.py $
# $Author: SkAsI.7 $
# $Id: problem0053.py 23 2011-01-19 12:21:17Z SkAsI.7 $
# $Revision: 23 $


# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import itertools
import optparse
import os
import sys
import time

# Internal imports (if any)

fact = lambda n: n == 0 and 1 or reduce(lambda a, b: a * b, xrange(1, n + 1))

def C(r, n, nf):
  return nf / fact(r) / fact(n - r)

def main():
  counter = 0
  for n in xrange(1, 101):
    nf = fact(n)
    for r in xrange(1, n + 1):
      if C(r, n, nf) > 1000000:
        counter += 1
  return counter


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

