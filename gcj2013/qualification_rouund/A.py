#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def check_config(config):
  config = set(config)

  if config == Xwon:
    return 'X'
  elif config == Owon:
    return 'O'
  else:
    return None

def config_generator(board):
  for i in xrange(0, 16, 4):
    yield board[i:i+4]

  for i in xrange(4):
    yield board[i::4]
  
  yield board[::5]
  yield board[3:15:3]

def challenge():
  lines = list()
  for _ in xrange(4):
    lines.append(getline())
  getline()

  board = ''.join(lines)
  draw = True
  for config in config_generator(board):
    config = set(config)
    if '.' in config:
      draw = False
      continue
    elif 'O' not in config:
      print 'X won'
      return
    elif 'X' not in config:
      print 'O won'
      return

  if draw:
    print 'Draw'
  else:
    print 'Game has not completed'

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

