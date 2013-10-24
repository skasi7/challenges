#!/usr/bin/python2.5
#-*- coding: utf-8 -*-

# Pychecker options
__pychecker__ = 'no-callinit no-classattr'

# External imports
import sys

# Internal imports (if any)

def getline():
  return sys.stdin.next().rstrip()

def backtracking(keys, chests, partial_solution):
  if not chests:
    return partial_solution

  # isSolutionReachable2
  potential_keys = set(keys) # keyTypes
  for k in potential_keys:
    owned_keys = keys.count(k) + sum([c[2].count(k) for c in chests])
    needed_keys = len(filter(lambda c: c[1] == k, chests))
    if owned_keys < needed_keys:
      return None
  ###

  # isSolutionReachable
  potential_keys = set(keys) # reachables
  needed_keys = set([c[1] for c in chests]) # keyTypes
  
  tested_keys = set() # reachabled
  key = 0
  while not tested_keys >= potential_keys:
    for k in potential_keys:
      if not k in tested_keys:
        key = k
        tested_keys.add(k)
        break
    potential_keys |= set(sum([c[2] for c in chests if c[1] == key], []))

  if not potential_keys >= needed_keys:
    return None
  ###

  for i, chest in enumerate(chests):
    n, key_type, chest_keys = chest
    if key_type in keys:
      new_keys = keys[::] + chest_keys
      new_keys.remove(key_type)
      new_chests = chests[:i] + chests[i+1:]
      solution = backtracking(new_keys, new_chests, partial_solution[::] + [n])
      if solution:
        return solution

  return None

def challenge():
  K, N = map(int, getline().split())
  keys = map(int, getline().split())
  chests = list()
  for i in xrange(N):
    tokens = map(int, getline().split())
    chest_keys = [] if tokens[1] == 0 else tokens[2:]
    chests.append((i + 1, tokens[0], chest_keys))

  solution = backtracking(keys, chests, [])
  if solution:
    print ' '.join(map(str, solution))
  else:
    print 'IMPOSSIBLE'

# Main entry point
if __name__ == '__main__':
  testcases = int(getline())

  for testcase in xrange(1, testcases + 1):
    print 'Case #%d:' % (testcase, ),
    challenge()

