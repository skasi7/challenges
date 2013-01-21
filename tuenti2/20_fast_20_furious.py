#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import itertools

def compute(r, k, groups):
  if r == 0:
    return 0
  
  k = min(k, sum(groups))

  cache = [(0, 0)] * len(groups)
  total = 0
  kartsLeft = k
  for i, g in enumerate(itertools.cycle(groups)):
    kartsLeft -= g

    if kartsLeft < 0:
      # Close the race without g

      total += k - kartsLeft - g
      r -= 1

      if not r:
        break

      kartsLeft = k - g

      if not cache:
        continue

      cacheIndex = i % len(groups)
      if cache[cacheIndex] != (0, 0):
        cacheElement = cache[cacheIndex]
        racesPerRound = cacheElement[0] - r
        litersPerRound = total - cacheElement[1]
        total += r / racesPerRound * litersPerRound
        r %= racesPerRound
        cache = [] # Disable the cache
      else:
        cache[cacheIndex] = (r, total)

      if not r:
        break

  return total

def main():
  lines = (line for line in sys.stdin)
  cases = int(lines.next())
  for testcase in xrange(cases):
    r, k, g = map(int, lines.next().split())
    groups = map(int, lines.next().split())[:g]
    print compute(r, k, groups)

if __name__ == '__main__':
  main()

