#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def get_candidates(n, m, board, node, i, j, visited, accum_value, max_Wm, candidates):
  c, cell_score, Wm = board[i][j]
  if (i, j) in visited or c not in node[1]:
    return

  visited = visited[::] + [(i, j)]
  accum_value += cell_score
  max_Wm = max(max_Wm, Wm)

  node = node[1].get(c)
  if node[0] is not None:
    candidates[node[0]] = \
        max(candidates.get(node[0], 0), accum_value * max_Wm + len(visited))

  if i < n:
    get_candidates(n, m, board, node, i+1, j, visited, accum_value, max_Wm, candidates)
    if j < m:
      get_candidates(n, m, board, node, i+1, j+1, visited, accum_value, max_Wm, candidates)
  if i > 0:
    get_candidates(n, m, board, node, i-1, j, visited, accum_value, max_Wm, candidates)
    if j > 0:
      get_candidates(n, m, board, node, i-1, j-1, visited, accum_value, max_Wm, candidates)
  if j < m:
    get_candidates(n, m, board, node, i, j+1, visited, accum_value, max_Wm, candidates)
    if i > 0:
      get_candidates(n, m, board, node, i-1, j+1, visited, accum_value, max_Wm, candidates)
  if j > 0:
    get_candidates(n, m, board, node, i, j-1, visited, accum_value, max_Wm, candidates)
    if i < n:
      get_candidates(n, m, board, node, i+1, j-1, visited, accum_value, max_Wm, candidates)
  

def challenge(root):
  scores = eval(getline())
  W = int(getline())
  n = int(getline())
  m = int(getline())
  board = list()
  for _ in xrange(n):
    row = list()
    # Cell: character, cell_score, WM
    for cell in map(tuple, getline().split()[:m]):
      cell_score = scores.get(cell[0])
      if cell[1] == '1': # CM
        cell = (cell[0], cell_score * int(cell[2]), 1)
      else: # cell[1] == 2: # WM
        cell = (cell[0], cell_score, int(cell[2]))
      row.append(cell)
    board.append(row)

  candidates = dict()
  for i in xrange(n):
    for j in xrange(m):
      get_candidates(n-1, m-1, board, root, i, j, [], 0, 1, candidates)

  candidates = sorted([(1.0 * s / (len(w) + 1), s, len(w) + 1)
    for w, s in candidates.iteritems()], reverse=True)
  # print candidates

  total_score = 0
  for rate, score, time in candidates:
    if W >= time:
      # print score, time, rate
      total_score += score
      W -= time
  # print 'seconds remaining', W
  print total_score

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  # Preprocess dictionary of words
  words = [w.strip() for w in open('boozzle-dict.txt', 'rb')]
  root = (None, dict())
  for word in words:
    word = word.strip()
    node = root[1]
    for c in word[:-1]:
      node = node.setdefault(c, (None, dict()))[1]
    node.setdefault(word[-1], (word, dict()))

  for testcase in xrange(1, testcases + 1):
    challenge(root)

