#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def challenge():
  tokens = map(int, getline().split())
  googlers, surprises, target = tokens[:3]
  scores = tokens[3:3 + googlers]

  min_score = max(3 * target - 2, target)
  min_surprise_score = max(3 * target - 4, target)

  result = 0
  for score in scores:
    if score >= min_score:
      result += 1
    elif score >= min_surprise_score and surprises > 0:
      result += 1
      surprises -= 1

  print result

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

