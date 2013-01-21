#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import itertools
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

lanes = dict(L=list(), R=list())

class Car:

  def __init__(self, position, speed):
    self.position = position
    self.speed = speed

  def __lt__(self, other):
    return self.position < other.position

  def __repr__(self):
    return '<Car Position: %d Speed: %d>' % (self.position, self.speed)

def candidates(lane):
  candidates = list()
  for c, d in itertools.izip(lane[:-1], lane[1:]):
    if c.speed <= d.speed:
      continue
    candidates.append(((d.position - c.position - 5.0) / (c.speed - d.speed), c))

  return candidates

def globalCandidates(L, R):
  L.sort()
  myCandidates = candidates(L)

  R.sort()
  myCandidates += candidates(R)

  myCandidates.sort()
  minTime = myCandidates[0][0]
  return [c for c in myCandidates if c[0] == minTime]

def simulate():
  L, R = lanes['L'], lanes['R']

  print globalCandidates(L, R)

def challenge():
  cars = int(getline())

  for car in xrange(cars):
    lane, speed, position = getline().split()
    speed, position = float(speed), float(position)

    lanes.get(lane).append(Car(position, speed))

  simulate()

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()
    break

