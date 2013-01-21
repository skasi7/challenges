#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys

def compute(prices):
  minimum = (0, prices[0])
  maximum = (0, 0)
  solution = (0, 0, 0)

  for i, price in enumerate(prices):
    if price < minimum[1]:
      minimum = (i, price)
      maximum = (0, 0)
    elif price > maximum[1]:
      maximum = (i, price)

    difference = maximum[1] - minimum[1]
    if difference > solution[2]:
      solution = (minimum[0], maximum[0], difference)

  print '%d %d %d' % (solution[0] * 100, solution[1] * 100, solution[2])

def main():
  prices = map(int, sys.stdin)
  compute(prices)

if __name__ == '__main__':
  main()

