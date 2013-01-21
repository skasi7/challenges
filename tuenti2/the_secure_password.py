#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import itertools
import copy

def topologicalSort(letters, partialOrderings, branch=None):
  L = []
  S = []
  for i in xrange(len(letters)):
    if sum([l[i] for l in partialOrderings]) == 0:
      S.append(i)

  branches = []

  while S:
    branches.append(range(len(S)))
    if branch:
      try:
        n = S.pop(branch.pop(0))
      except IndexError:
        return
    else:
      n = S.pop()
    L.append(n)
    for m in [i for i, x in enumerate(partialOrderings[n]) if x]:
      partialOrderings[n][m] = 0
      if sum([l[m] for l in partialOrderings]) == 0:
        S.append(m)

  if branch is not None:
    return L
  else:
    return branches

def compute(subcodes):
  letters = list(set(''.join(subcodes)))

  partialOrderings = []
  for _ in letters:
    partialOrderings.append([0] * len(letters))

  for subcode in subcodes:
    subcode = [letters.index(c) for c in subcode]
    partialOrderings[subcode[0]][subcode[1]] = 1
    partialOrderings[subcode[1]][subcode[2]] = 1

  candidates = []
  for branch in itertools.product(
      *topologicalSort(letters, copy.deepcopy(partialOrderings))):
    candidate = topologicalSort(letters, copy.deepcopy(partialOrderings)
        , list(branch))
    if candidate is not None:
      candidates.append(''.join([letters[i] for i in candidate]))

  candidates.sort()

  for candidate in candidates:
    print candidate

def main():
  subcodes = [s.strip() for s in sys.stdin]
  compute(subcodes)

if __name__ == '__main__':
  main()

