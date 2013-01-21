#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# subversion info:
# $HeadURL: https://skasi-lps.googlecode.com/svn/trunk/euler/problem0081.py $
# $Author: SkAsI.7 $
# $Id: problem0081.py 29 2011-01-31 14:32:25Z SkAsI.7 $
# $Revision: 29 $


# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import itertools
import optparse
import os
import sys
import time

# Internal imports (if any)


def minimal_path(data):
  new_data = list()
  for i, row in enumerate(data):
    new_row = list()
    for j, element in enumerate(row):
      subpaths = list()
      if i > 0:
        subpaths.append(new_data[i - 1][j])
      if j > 0:
        subpaths.append(new_row[j - 1])
      if not subpaths:
        subpaths.append(0)
      new_row.append(element + min(subpaths))
    new_data.append(new_row)
  return new_data[i][j]

def main():
  try:
    filename = args[0]
  except IndexError:
    filename = 'matrix0081.txt'

  try:
    data = open(filename).readlines()
    data = [map(int, line.strip().split(',')) for line in data]
    return minimal_path(data)
  except IOError:
    return 'Unable to read filename "%s"' % filename


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

