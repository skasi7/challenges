#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def config_generator(N, M, lawn):
  for i in xrange(0, N * M, M):
    yield lawn[i:i+M]

  for i in xrange(M):
    yield lawn[i::M]

def challenge():
  N, M = map(int, getline().split())

  lawn = list()
  for _ in xrange(N):
    lawn += map(int, getline().split())
  
  heights = list()
  for config in config_generator(N, M, lawn):
    heights.append(max(config))

  for Yheight in heights[:N]:
    for Xheight in heights[N:N+M]:
      if lawn.pop(0) not in (Xheight, Yheight):
        print 'NO'
        return
  print 'YES'

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

