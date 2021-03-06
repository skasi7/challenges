#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# subversion info:
# $HeadURL: https://skasi-lps.googlecode.com/svn/trunk/euler/problem0052.py $
# $Author: SkAsI.7 $
# $Id: problem0052.py 23 2011-01-19 12:21:17Z SkAsI.7 $
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

def compare(base):
  ns = [base * i for i in xrange(1, 7)]
  s_digits = [int(c) for c in str(ns.pop())]
  s_digits.sort()
  for n in ns:
    n_digits = [int(c) for c in str(ns.pop())]
    n_digits.sort()
    if n_digits != s_digits:
      return False
  return True

def main():
  for n in itertools.ifilter(compare, itertools.count(1)):
    return n


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

