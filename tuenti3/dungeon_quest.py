#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import operator
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def best(M, N, board, X, Y, seconds, partial):
  if seconds == 1:
    return [board[X][Y-1] if Y > 0 else 0
        , board[X][Y+1] if Y < N else 0
        , board[X+1][Y] if X < M else 0
        , board[X-1][Y] if X > 0 else 0]
  
  values = list()
  # North
  if Y > 0:
    values.append(board[X][Y] + best(M, N, board, X, Y-1, seconds - 1, partial + [(X, Y)]))
  else:
    values.append(board[X][Y])
  # South

  # East

  # West

def challenge():
  M, N = map(int, getline().split(','))
  board = [[0] * M for _ in xrange(N)]

  X, Y = map(int, getline().split(','))
  Z = int(getline())
  G = int(getline())

  for x, y, v in [tuple(map(int, g.split(','))) for g in getline().split('#')[:G]]:
    board[x][y] = v

  print best(M - 1, N - 1, board, X, Y, Z, [])

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    challenge()

