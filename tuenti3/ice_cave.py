#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def way_out(my_map, S, T, X, Y, Xd, Yd, visited, time):
  x, y = X, Y
  cell = my_map[x][y]
  while cell == '.':
    x += Xd
    y += Yd
    cell = my_map[x][y]

  # Fix the rock
  x -= Xd
  y -= Yd

  mov = abs(x - X) + abs(y - Y)
  time += mov / S
  # print 'Moving', Xd, Yd, 'during', mov, 'cells'

  if cell == 'O': # Out!
    return time + 1.0 / S

  if (x, y) in visited: # Already here
    return 999999
  visited += [(x, y)]

  time += T
  if Xd == 0:
    # Moves +1, 0 or -1, 0
    # print 'Moving N-S'
    return min(
        way_out(my_map, S, T, x, y, +1, 0, visited, time),
        way_out(my_map, S, T, x, y, -1, 0, visited, time))
  else: # Yd == 0
    # Moves 0, +1 or 0, -1
    # print 'Moving E-W'
    return min(
        way_out(my_map, S, T, x, y, 0, +1, visited, time),
        way_out(my_map, S, T, x, y, 0, -1, visited, time))

def challenge():
  W, H, S, T = map(int, getline().split())
  S, T = float(S), float(T)
  my_map = list()
  for y in xrange(H):
    row = getline().replace('\xc2\xb7', '.')[:W]
    if 'X' in row:
      X, Y = y, row.index('X')
      row = row.replace('X', '.')
    my_map.append(row)

  """
  for row in my_map:
    print row
  """

  # South move
  print int(round(min(
      way_out(my_map, S, T, X, Y, +1, 0, [(X, Y)], T),
      way_out(my_map, S, T, X, Y, -1, 0, [(X, Y)], T),
      way_out(my_map, S, T, X, Y, 0, +1, [(X, Y)], T),
      way_out(my_map, S, T, X, Y, 0, -1, [(X, Y)], T))))
  
# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    challenge()

