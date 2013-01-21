#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# Special thanks to safull by the tips

import sys
import datetime

# Transitions between digits
oldClock = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
  }

newClock = {
    ('0', '0'): 0,
    ('0', '1'): 0,
    ('0', '2'): 1,
    ('0', '3'): 1,
    ('0', '4'): 1,
    ('0', '5'): 1,
    ('0', '6'): 1,
    ('0', '7'): 0,
    ('0', '8'): 1,
    ('0', '9'): 1,
    ('1', '2'): 4,
    ('2', '3'): 1,
    ('3', '4'): 1,
    ('4', '5'): 2,
    ('5', '6'): 1,
    ('6', '7'): 1,
    ('7', '8'): 4,
    ('8', '9'): 0,
    ('9', '0'): 1,
    ('2', '0'): 2,
    ('3', '0'): 2,
    ('5', '0'): 2
  }

def computeTimeDiff(s, e, timeFormat='%H%M%S'):
  if s.time() == e.time():
    return 0

  secondDelta = datetime.timedelta(seconds=1)

  total = 0

  currentTime = s
  currentRepr = currentTime.strftime(timeFormat)
  while True:
    currentTime += secondDelta

    stringRepr = currentTime.strftime(timeFormat)

    oldLeds = sum([oldClock[c] for c in stringRepr])
    newLeds = sum([newClock[t] for t in zip(currentRepr, stringRepr)
      if t[0] != t[1]])
    total += oldLeds - newLeds

    if currentTime.time() == e.time():
      break

    currentRepr = stringRepr

  return total

"""
print computeTimeDiff(datetime.datetime(1900, 1, 1, 0)
    , datetime.datetime(1900, 1, 1, 12)) \
        + computeTimeDiff(datetime.datetime(1900, 1, 1, 12)
            , datetime.datetime(1900, 1, 1, 0))
"""
# Computed using the previous expression
dayLeds = 2255477 

def compute(startDate, endDate):
  total = -36

  # From 00:00:00 to startDate
  total += sum([oldClock[i] - newClock[('0', i)]
    for i in startDate.strftime('%H%M%S')])

  # From startDate to endDate
  diffDate = endDate - startDate
  total += diffDate.days * dayLeds \
      + computeTimeDiff(startDate, endDate)

  return total

def main():
  for line in sys.stdin:
    startDate, endDate = line.split(' - ')
    startDate = datetime.datetime.strptime(startDate.strip()
        , '%Y-%m-%d %H:%M:%S')
    endDate = datetime.datetime.strptime(endDate.strip()
        , '%Y-%m-%d %H:%M:%S')
    print compute(startDate, endDate)

if __name__ == '__main__':
  main()

