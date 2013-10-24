#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def challenge():
  W, H, Sc, Cc, G = map(int, getline().split())

  if G / Sc >= W: # Forever
    print -1
    return

  survival_time = 0
  for S in xrange(G / Sc + 1):
    C = (G - Sc * S) / Cc
    # print S, 'soldiers', C, 'crematoriums'
    # print 'survival time', (W * (H - 1) / (W - S) + 1) * (C + 1)
    survival_time = max(survival_time,
        (W * (H - 1) / (W - S) + 1) * (C + 1))
  print survival_time

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    challenge()

