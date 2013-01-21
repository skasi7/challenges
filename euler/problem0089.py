#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# subversion info:
# $HeadURL: https://skasi-lps.googlecode.com/svn/trunk/euler/problem0089.py $
# $Author: SkAsI.7 $
# $Id: problem0089.py 30 2011-01-31 16:47:42Z SkAsI.7 $
# $Revision: 30 $


# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import itertools
import optparse
import os
import sys
import time

# Internal imports (if any)


def optimize_roman(numeral):
  new_numeral = numeral
  new_numeral = new_numeral.replace('DCCCC', 'CM')
  new_numeral = new_numeral.replace('CCCC', 'CD')
  new_numeral = new_numeral.replace('LXXXX', 'XC')
  new_numeral = new_numeral.replace('XXXX', 'XL')
  new_numeral = new_numeral.replace('VIIII', 'IX')
  new_numeral = new_numeral.replace('IIII', 'IV')
  return len(numeral) - len(new_numeral)

def main():
  try:
    filename = args[0]
  except IndexError:
    filename = 'roman0089.txt'

  data = [line.strip() for line in open(filename).readlines()]
  return sum(map(optimize_roman, data))


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

