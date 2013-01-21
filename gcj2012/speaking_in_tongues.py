#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import string
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

transtable = string.maketrans(
  'abcdefghijklmnopqrstuvwxyz',
  'yhesocvxduiglbkrztnwjpfmaq')
def challenge():
  print getline().translate(transtable)

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

