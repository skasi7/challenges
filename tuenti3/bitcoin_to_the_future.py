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
  amount = int(getline())
  rates = map(int, getline().split()) + [None]
  prev_rate = buy_rate = rates[0]
  for rate in rates[1:]:
    if rate is None or rate < prev_rate: # Decreasing
      if buy_rate < prev_rate:
        # Sell
        amount *= prev_rate
        amount /= buy_rate
      buy_rate = rate
    prev_rate = rate
  print amount

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    challenge()

